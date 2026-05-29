class Notifier:
    def send(self,message):
        pass

class Emailnotifier(Notifier):
    def send(self,message):
        print(f"sending Email:{message}")

class SMSNotifier(Notifier):
    def send(self,message):
        print(f"Sending SMS:{message}") 

class PushNotifier(Notifier):
    def send(self,message):
        print(f"sending Push notification:{message}")   

def process_notification(notifier,message):
    notifier.send(message) 

email=Emailnotifier()
sms=SMSNotifier()
push=PushNotifier()


process_notification(email,"Welcome User !")
process_notification(sms,"OTP is 8371")    
process_notification(push,"You have a new message")