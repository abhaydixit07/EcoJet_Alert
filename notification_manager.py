# from twilio.rest import Client
# auth_token="54b4fd312061d06d7d91e2397fbdc457"
# account_sid="AC8c897ee9227f9b9c90aa716030c1cb24"
import smtplib
MY_EMAIL = 'abhaydixitfake@gmail.com'
MY_PASS = 'pzmyktvgocakvtsb'
# class NotificationManager:
#     def __init__(self):
#         pass
def send_email(to_addrs,mesg):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASS)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_addrs, msg=f"Subject:Low💰 Price Alert🚨!\n\n{mesg}".encode('utf-8'))




    # def send_sms(self, msg):
        

    #     client = Client(account_sid, auth_token)
    #     message = client.messages.create(
    #             body=msg,
    #             from_='+17622496046',
    #             to='+918287467417'
    #         )
    #     print(message.status)

    
        
