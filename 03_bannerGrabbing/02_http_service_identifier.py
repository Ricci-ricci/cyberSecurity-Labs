import argparse
import socket


def grab_http_banner(ip, port):
    """
    Connects to a web server and sends a specific HTTP trigger to get a response.
    Unlike standard banner grabbing, web servers require an initial request.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        print(f"[*] Connecting to {ip} on port {port}...")
        s.connect((ip, port))

        #  we trigger it because Web servers are 'shy' and wait for the client to speak first.
        # We send a standard HTTP HEAD request.
        # HEAD retrieves only headers (metadata) without the body (HTML), which is faster.
        trigger = f"HEAD / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: PythonScanner/1.0\r\nConnection: close\r\n\r\n"

        s.send(trigger.encode())

        # Receive response
        response = s.recv(4096).decode("utf-8", errors="ignore")
        s.close()
        return response

    except socket.timeout:
        return "Error: Connection timed out."
    except ConnectionRefusedError:
        return "Error: Connection refused."
    except Exception as e:
        return f"Error: {str(e)}"


def identify_server_software(http_response):
    """
    Parses the raw HTTP response headers to identify the server software.
    """
    if not http_response or "Error:" in http_response:
        return None

    lines = http_response.split("\r\n")

    # Iterate through headers to find the 'Server' field
    for line in lines:
        if line.lower().startswith("server:"):
            # Split by the first colon and strip whitespace
            return line.split(":", 1)[1].strip()

    return "Unknown (Server header not found)"


def main():
    # Using argparse to handle command line arguments
    parser = argparse.ArgumentParser(
        description="HTTP Service Identifier (Trigger & Identify)"
    )

    parser.add_argument(
        "-t", "--target", required=True, help="Target IP address or Hostname"
    )
    parser.add_argument(
        "-p", "--port", type=int, default=80, help="Target port (default: 80)"
    )

    args = parser.parse_args()

    # Run the grabber
    raw_response = grab_http_banner(args.target, args.port)

    if raw_response.startswith("Error"):
        print(f"[-] {raw_response}")
    else:
        # Run the identifier
        server_id = identify_server_software(raw_response)

        print("[+] HTTP Handshake Successful")
        print("-" * 50)
        print(
            f"Identified Server Software: \033[1;32m{server_id}\033[0m"
        )  # Green text for visibility
        print("-" * 50)

        # Show raw headers for context
        print("\n[Raw Response Headers Preview]")
        header_end = raw_response.find("\r\n\r\n")
        if header_end != -1:
            print(raw_response[:header_end])
        else:
            print(raw_response[:500])  # Print first 500 chars if structure is weird


if __name__ == "__main__":
    main()
