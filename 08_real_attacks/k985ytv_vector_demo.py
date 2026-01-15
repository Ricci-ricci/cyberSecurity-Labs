"""
This script demonstrates the infection vector of the K985ytv worm, which exploited the MS08-067 vulnerability in Windows SMB service.

Inspired by the book "Violent Python" by TJ O'Connor. I learned a lot from this book and highly recommend it: https://www.nostarch.com/violentpython.

For educational purposes only. Do not use on systems you do not own or have permission to test. This is a simplified demo and does not perform actual exploitation.
"""

import socket
import struct
import sys

# This is a mock demo of the MS08-067 exploit vector
# In reality, this would use a full exploit payload, but here we just demonstrate the connection attempt


def exploit_ms08_067(target_ip, target_port=445):
    """
    Mock function to demonstrate the MS08-067 infection vector.
    The real K985ytv worm used this to spread via SMB.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((target_ip, target_port))
        print(f"[+] Connected to {target_ip}:{target_port} (SMB port)")

        # In a real exploit, this would send a crafted SMB packet to trigger the vulnerability
        # For demo, we just send a simple message
        message = b"Hello from K985ytv demo"
        sock.send(message)
        response = sock.recv(1024)
        print(f"[+] Response: {response}")

        sock.close()
        print(
            "[+] Demo complete. In reality, this could lead to code execution and infection."
        )

    except socket.error as e:
        print(f"[-] Connection failed: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python k985ytv_vector_demo.py <target_ip>")
        sys.exit(1)

    target = sys.argv[1]
    print("Demonstrating K985ytv infection vector (educational only)")
    exploit_ms08_067(target)
