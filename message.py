import datetime
class Message:

    '''
    
    Created by Travis Tran on July 24, 2023

    This is the message class for the chat application problem
    
    The message class (in a chatroom) is defined by 5 unique features:

    1) sender (client ID) - string
    2) payload (the actual message) - string
    3) timestamp - a date
    4) chatroom ID - string
    5) unique ID - string

    See https://blksail-edu.github.io/docs/module/networking#mdns for more details of the other classes and python files involved in this problem
    
    '''


    #class fields
    sender = ''
    payload = ''
    timestamp = datetime.now()
    chatroom_id = ''
    uuid = ''

    #constructor
    def __init__ (self, sender, payload, timestamp, chatroom_id):
        self.sender = sender
        self.payload = payload
        self.timestamp = timestamp
        self.chatroom_id = chatroom_id
        self.uuid = sender+'_'+timestamp.strftime()+'_'+chatroom_id+'_'+len(payload)
    
    # Allows the message to be edited (might not allow other users to see the new message tho)
    def setPayload(self, newPayload):
        self.payload = newPayload
        self.timestamp = datetime.now() #time resets if message is edited
        self.uuid = self.sender+'_'+self.timestamp.strftime()+'_'+self.chatroom_id+'_'+len(self.payload) #uuid gets recreated if message is edited
