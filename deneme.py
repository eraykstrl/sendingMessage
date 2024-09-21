import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = "192.168.137.115"
port = 8000
message = "kamikaze"

sock.sendto(message.encode(), (server, port))
