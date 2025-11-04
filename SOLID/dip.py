# Before DIP
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")
class SMSService:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")
class Notification:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()

    def send(self, message, method):
        if method == "email":
            self.email_service.send_email(message)
        elif method == "sms":
            self.sms_service.send_sms(message)
if __name__ == '__main__':
    my_notifier = Notification()
    my_notifier.send("Salam", "email")
