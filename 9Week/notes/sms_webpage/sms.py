from twilio.rest import Client
import json

with open('creds.json', 'r') as infile:
    creds = json.load(infile)

def send_text(data):
    sid = creds['twilio_sid']
    token = creds['twilio_token']
    client = Client(sid, token)
    numbers = [#'+14152382494','+19175156779','+13107390178',
    '+15615989709','+14152382494']
    for number in numbers:
        message = client.messages.create(
         to=number,
         from_='+13472464454',
         body=data
    )
