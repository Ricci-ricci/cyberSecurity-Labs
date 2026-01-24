import argparse
import socket
import sys


def grab_banner(ip, port):
    """
    Attempts to connect to the specified IP and port to retrieve a service banner.
    """
    try:
        # Create a socket object (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout so the script doesn't hang indefinitely if the server is silent
        s.settimeout(2)

        print(f"[*] Connecting to {ip} on port {port}...")
        s.connect((ip, port))

        # Receive up to 1024 bytes of data
        # Note: This works best for 'chatty' protocols like SSH, FTP, SMTP
        banner = s.recv(1024)

        # Close the connection
        s.close()

        # Decode bytes to string, ignoring errors for non-printable characters
        return banner.decode("utf-8", errors="ignore").strip()

    except socket.timeout:
        return "Error: Connection timed out. The service might not be sending a banner automatically."
    except ConnectionRefusedError:
        return "Error: Connection refused. The port might be closed."
    except Exception as e:
        return f"Error: {e}"


def main():
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Simple TCP Banner Grabber")

    # Add arguments
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--port", type=int, required=True, help="Target port")

    # Parse arguments
    args = parser.parse_args()

    # Execute banner grab
    banner = grab_banner(args.target, args.port)

    # Display results
    if banner:
        print(f"[+] Banner received from {args.target}:{args.port}")
        print("-" * 40)
        print(banner)
        print("-" * 40)
    else:
        print("[-] No data received.")


if __name__ == "__main__":
    main()
