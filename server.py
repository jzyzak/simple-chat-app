#import socket

class Server:
    ip_address = ""
    port = 0
    
    def __init__(self, ip:str, port:int):
        '''Initializing the Server class
        Parameter:
            ip_address- the ip address of the computer hosting the server
            port- the port of the socket, ranging from 6000 and 49000'''
        self.ip_address = ip
        self.port = port
        #if port not in range(6000,49000):
            #raise ValueError
        #split = ip.split(".")
        #for num in split:
            #if num not in range(0,256):
                #raise ValueError
            
"""
    def verifyIP(self, IP):
        '''Verifying that IP exists
        Parameters:
            IP- ip address that is going to be verified
        Returns a boolean value based on whether the ip address exists on the current internet'''
        try:
            socket.inet_aton(IP)
        except Exception as e:
            return False
        return True
"""