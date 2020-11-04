import socket
import threading

#size of messages in bytes to be recieved by the socket server. Must be fixed
HEADER = 64
#The port the socket server runs on
PORT = 8080
#The computer's IPv4 address
SERVER = socket.gethostbyname(socket.gethostname())

#The address the socket is connected to. Must be a Tuple.
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
#Message to be sent by client when wanting to disconnect
DISCONNECT_MESSAGE = "!DISCONNECT"

#The socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind the address to the server
server.bind(ADDRESS)

#Function to handle client connection
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Messaged recieved by server".encode(FORMAT))
    
    conn.close()




def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
