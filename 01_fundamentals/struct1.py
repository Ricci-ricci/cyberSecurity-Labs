import socket
import struct 

host = "0.0.0.0"
port = 12345

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
	s.bind((host , port))
	s.listen(1)
	print(f"listening on {host} on port {port}")
	conn , addr = s.accept()
	with conn : 
		print(f"Connected by {addr}")
		msg = struct.pack("hhl" , 1 , 2 , 3)
		conn.sendall(msg)