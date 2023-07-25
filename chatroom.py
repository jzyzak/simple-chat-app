from client import Client
from message import Message

class Chatroom:
    name = ""
    uuid = ""
    msgList = []
    clients = []

    def __init__(self, n, id, messages : list, clients : list):
        self.name = n
        self.uuid = id
        self.msgList = messages
        self.clients = clients

    def sendMsg(self, message : Message):
        usernameList = [user.username for user in self.clients]
        #if(self.uuid == message.chatroom_id):
        for i in range(0, len(self.clients)):
            if(self.uuid == message.chatroom_id and message.sender in usernameList):
                self.msgList.append(message)                

    def addClient(self, client : Client):
        if (client in self.clients) == False:
            self.clients.append(client)

    def removeClient(self, client : Client):
        if (client in self.clients):
            self.clients.remove(client)
