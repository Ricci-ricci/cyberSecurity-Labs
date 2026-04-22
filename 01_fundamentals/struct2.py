import socket
import struct
host = "127.0.0.1"
port = 12345
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
	s.connect((host , port))
	data = s.recv(1024)
	values = struct.unpack("hhl" , data)
	print(values)