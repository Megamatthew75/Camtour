# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

new_key = client.new_keys.create(friendly_name='User Joey')

message = client.messages \
                .create(
                     messaging_service_sid='MG762b7ed5e3a8230db969eae41897715d',
                     body="Booyah",
                     to='+12488809854'
                 )

print(message.sid)
