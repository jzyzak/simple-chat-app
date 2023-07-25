# Client class with client attributes/information
class Client:
    username = ""
    ip_address = ""
    password = ""
    uuid = ""

    # Constructor for client class
    def __init__(self, user, ip, pw, id):
        self.username = user
        self.ip_address = ip
        self.password = pw
        self.uuid = id
