
# Message Sender

from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailSender(MessageSender):
    def send(self):
        return "Sending Email..."

class SMSSender(MessageSender):
    def send(self):
        return "Sending SMS..."

def notify(sender):
    print(sender.send())

notify(EmailSender())   
notify(SMSSender())     
