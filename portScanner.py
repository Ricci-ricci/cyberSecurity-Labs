import optparse
import socket
import threading

screenLock = threading.Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    connSkt = None
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b"ViolentPython\r\n")
        results = connSkt.recv(100)
        with screenLock:
            print("[+]%d/tcp open" % tgtPort)
            print("[+]" + str(results))
    except Exception:
        with screenLock:
            print("[-]%d/tcp closed" % tgtPort)
    finally:
        if connSkt:
            connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except socket.gaierror:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print("\n[+] Scan Results for: " + tgtName[0])
    except socket.herror:
        print("\n[+] Scan Results for: " + tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print("Scanning port " + str(tgtPort))
        connScan(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser(
        "usage%prog" + "-t <target host> -p <target port(s)>"
    )
    parser.add_option("-t", dest="tgtHost", type="string", help="specify target host")
    parser.add_option(
        "-p",
        dest="tgtPorts",
        type="string",
        help="specify target port(s) separated by comma",
    )
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(",")
    if tgtHost == None or tgtPorts[0] == None:
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == "__main__":
    main()
