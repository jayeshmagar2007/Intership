'''Abstract Class as an Interface
Instructions:

Create an abstract class named Notification with abstract method:

send_message().

Create concrete classes:

EmailNotification

SMSNotification

PushNotification

Create instances of each class and call send_message() in a loop.'''


from abc import ABC ,abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_message(self):
        pass

class EmailNotification(Notification):
    def send_message(self):
        print("new E mail...")
class SMSNotification(Notification):
    def send_message(self):
        print("New sms...")

class PushNotification(Notification):
    def send_message(self):
        print("your notification had been pushed..")

notif = [EmailNotification(),SMSNotification(),PushNotification()]
for i in notif :
    i.send_message()


