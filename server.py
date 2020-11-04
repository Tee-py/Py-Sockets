import socket
import threading

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())


print(SERVER)