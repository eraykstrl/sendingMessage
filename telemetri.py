import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = "192.168.137.104"
port = 8001
message = "ahmet"
message2="kamikaze"
port2=8000
sock.sendto(message2.encode(), (server, port2))
while True:
    sock.sendto(message.encode(), (server, port))
    time.sleep(1)
