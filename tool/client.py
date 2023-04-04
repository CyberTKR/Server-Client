import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.message = None
        
    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        
        print(f"Server listening on {self.host}:{self.port}")
        
        self.client_socket, _ = self.server_socket.accept()
        self.message = self.client_socket.recv(1024).decode()
        
        print(f"Received message: {self.message}")
        
        self.client_socket.close()
        self.server_socket.close()
        
class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None
        
    def send_message(self, message):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        
        self.client_socket.send(message.encode())
        
        print(f"Sent message: {message}")
        
        self.client_socket.close()
