import socket

HOST = "127.0.0.1"
PORT = 8000
TIMEOUT = 2.0


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        try:
            s.connect((HOST, PORT))
            print(f"connected to host {HOST} {PORT} ")
        except (socket.timeout, ConnectionRefusedError) as e:
            print(f"failet to connect : {e}")


if __name__ == "__main__":
    main()
