import socket

class Client:
    def __init__(self):
        self.server_ip="10.91.47.74"  # You can enter the IP address of the server computer here.
        self.port=81

    def client(self):
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
        message="you can send every message from here"
        while True:
            try:
                client_socket.sendto(message.encode(),(self.server_ip,self.port))
            
            except Exception as e:
                pass

            finally:
                client_socket.close()

client=Client()
client.client()
        
