class Client:
    username = ""
    ip_address = ""
    password = ""
    uuid = ""

    def __init__(self, user, ip, pw, id):
        self.username = user
        self.ip_address = ip
        self.password = pw
        self.uuid = id
