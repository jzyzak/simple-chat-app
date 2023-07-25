from server import Server
from client import Client
import socket
import _thread

serverIP = "10.31.7.146"
serverPort = 8432
serverClients = {}

# Could probably add prompt to ask user to input the server IP address and server port number

server = Server(serverIP, serverPort) # creates the server object

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates the server socket
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # fixes issue with opening/closing too many connections too frequently by allowing the server IP address to be reused
serverSocket.bind((serverIP, serverPort)) # binds the server socket to the given IP address and port number

# Function to broadcast messages from server clients to all other clients
def broadcastMessages(message, addr):
    print(message)
    for client in serverClients:
        if(addr[0] != client):
            #serverClients[client][0].send((serverClients[addr[0]][1] + ": " + message).encode())
            serverClients[client][0].send(message.encode())
            #serverSocket.send((serverClients[addr[0]][1] + ": " + message).encode())
            #serverSocket.sendall((serverClients[addr[0]]))
            #serverSocket.sendto((serverClients[client][1] + ": " + message).encode(), addr)

def acceptClientsAndMessages(conn, addr):
    while True:
        data = conn.recv(1024)
        msg = data.decode()
        if(msg[0:4] == "INFO"):
            userInformation = msg[6:].split(" ")
            serverClients[addr[0]].append(userInformation[0])
            serverClients[addr[0]].append(userInformation[1])
            print("successfully added user " + serverClients[addr[0]][1])
        else:
            broadcastMessages(msg, addr)

while True:
    serverSocket.listen(5)
    conn, addr = serverSocket.accept()
    serverClients[addr[0]] = [conn]
    _thread.start_new_thread(acceptClientsAndMessages, (conn, addr))
