from client import Client
import _thread
import socket
import uuid

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Can ask user to input later
server_ip = "10.31.7.146"
server_port = 8432

clientUsername = ""
while(len(clientUsername) == 0):
    clientUsername = input("Please enter a valid username: ")
clientIP = socket.gethostbyname(socket.gethostname())
clientPassword = ""
while(len(clientPassword) == 0):
    clientPassword = input("Pleas enter a valid password: ")
clientUUID = uuid.uuid1()

currentClient = Client(clientUsername, clientIP, clientPassword, clientUUID)

clientSocket.connect((server_ip, server_port))

def sendingMessages():
    userInfo = "INFO: " + clientUsername + " " + "clientUUID"
    clientSocket.send(userInfo.encode())

    while True:
        message = input(clientUsername + ": ")
        message = clientUsername + ": " + message
        clientSocket.send(message.encode())

_thread.start_new_thread(sendingMessages(), ())

while True:
    print("received something")
    message = clientSocket.recv(2048)
    print(message.decode())