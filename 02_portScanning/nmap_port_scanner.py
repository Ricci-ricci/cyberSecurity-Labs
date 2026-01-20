import optparse

import nmap


def nmapScan(tgtHost, tgtPort):
    nmscan = nmap.PortScanner()
    nmscan.scan(tgtHost, tgtPort)
    state = nmscan[tgtHost]["tcp"][int(tgtPort)]["state"]
    print(f"[+] {tgtHost} tcp/{tgtPort} {state}")


def main():
    parser = optparse.OptionParser("usage%prog " + "-H <Target host> -p <Target port>")
    parser.add_option("-H", dest="tgtHost", type="string", help="Specify target host")
    parser.add_option(
        "-p", dest="tgtPorts", type="string", help="specify all the Target ports"
    )
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = options.tgtPorts

    if tgtHost is None or tgtPorts is None:
        print(parser.usage)
        exit(0)

    for tgtPort in tgtPorts.split(","):
        nmapScan(tgtHost, tgtPort.strip())


if __name__ == "__main__":
    main()
