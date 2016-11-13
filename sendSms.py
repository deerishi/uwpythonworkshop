from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)
f=open('phoneNumbers','r')
numbers=[]
for line in f:
    numbers.append(line.split('\n')[0])

for number in numbers:
    try:
        message = client.messages.create(body="The name's Bond,.... James Bond",to=number,from_="+12268940383")
        print('SMS sent to ',number)
    except TwilioRestException as e:
        print(e)
