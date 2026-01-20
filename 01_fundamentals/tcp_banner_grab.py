import optparse
import socket


def grab_banner(host, port):
    try:
        with socket.create_connection((host, port)) as s:
            s.settimeout(2.0)
            try:
                data = s.recv(1024)
            except socket.timeout:
                return b""
            return data
    except (ConnectionRefusedError, OSError):
        return b""


def main():
    parser = optparse.OptionParser("usage: %prog -H <host> -p <port>")
    parser.add_option("-H", dest="host", type="string", help="specify target host")
    parser.add_option("-p", dest="port", type="int", help="specify target port")
    (options, args) = parser.parse_args()
    host = options.host
    port = options.port
    if host is None or port is None:
        print(parser.usage)
        exit(0)
    banner = grab_banner(host, port)
    if banner:
        print(f"Banner from {host}:{port} - {banner.decode().strip()}")
    else:
        print(f"No banner received from {host}:{port}")


if __name__ == "__main__":
    main()
