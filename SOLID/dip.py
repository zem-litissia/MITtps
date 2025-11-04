from abc import ABC, abstractmethod
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")
class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")
class PushService(NotificationService):
    def send(self, message):
        print(f"Sending push notification: {message}")
class Notification:
    def __init__(self, service: NotificationService):
        self.service = service
    def send(self, message):
        self.service.send(message)
if __name__ == '__main__':
    # Email
    email_service = EmailService()
    notification = Notification(email_service)
    notification.send("Hello via Email!")
    # SMS
    sms_service = SMSService()
    notification = Notification(sms_service)
    notification.send("Hello via SMS!")
    # Push
    push_service = PushService()
    notification = Notification(push_service)
    notification.send("Hello via Push Notification!")
