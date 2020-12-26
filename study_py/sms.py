#+18048861141

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
TWILIO_ACCOUNT_SID = 'ACfc4068630a049b211c41d70fe2e83970'
TWILIO_AUTH_TOKEN = 'bf0599bf65d51f393c699459b38be799'


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages \
                .create(
                     body="Hello, I'm Jaehyun! Do python! Fighting!",
                     from_='+18048861141',
                     to='+821020678057'
                 )

print(message.sid)