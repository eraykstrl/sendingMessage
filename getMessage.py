import socket

class Server:

    def __init__(self):
        self.adress=("0.0.0.0",81) #you can enter localhost here
        #this port should be same client port adress

    def server(self):
        server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        server_socket.bind(self.adress)

        while True:
            data,adress=server_socket.recvfrom(1024)
            message=data.decode('utf-8')
            print("Received message is ", message)

server=Server()
server.server()