import random
from twilio.rest import Client

otp = random.randint(1000, 9999)

account_sid = "ACd3bfdbbd10cd1adda8325c4c38295f17"
auth_token = 'a5d06567b6c898bae52a809b4b65e5c0'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body=f"Your OTP is {otp}",
    from_="+14692084423",
    to="+918080202882"
)

user_otp = input("Enter the OTP sent to your phone: ")

if user_otp == str(otp):
    print("OTP is valid. Access granted.")
else:
    print("OTP is invalid. Access denied")