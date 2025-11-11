from abc import ABC, abstractmethod

# --- Logger abstraction ---
class ILogger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(ILogger):
    def log(self, message):
        print(f"Logging to file: {message}")

class DatabaseLogger(ILogger):
    def log(self, message):
        print(f"Logging to database: {message}")

# --- Notification abstraction ---
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

# --- High-level Notification class ---
class Notification:
    def __init__(self, service: NotificationService, logger: ILogger):
        self.service = service
        self.logger = logger

    def send(self, message):
        self.service.send(message)
        self.logger.log(f"Notification sent: {message}")

# --- Main call ---
if __name__ == '__main__':
    # Using FileLogger
    file_logger = FileLogger()

    # Email notification
    email_service = EmailService()
    notification = Notification(email_service, file_logger)
    notification.send("Hello via Email!")

    # SMS notification
    sms_service = SMSService()
    notification = Notification(sms_service, file_logger)
    notification.send("Hello via SMS!")

    # Push notification
    push_service = PushService()
    notification = Notification(push_service, file_logger)
    notification.send("Hello via Push Notification!")

    # Using DatabaseLogger with PushService
    db_logger = DatabaseLogger()
    notification_db = Notification(push_service, db_logger)
    notification_db.send("Hello via Push with DB logger!")
