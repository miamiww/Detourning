from envelopes import Envelope
from questions import get_random_question
import json

with open('creds.json', 'r') as infile:
    creds = json.load(infile)


text = get_random_question().upper()

html = '<b style = "font-size: 100px; color: white; background-color: red;">' + text + '</b>'

message = Envelope(
    from_addr=("detourning2018@gmail.com", "lol"),
    to_addr=("arj247@nyu.edu", "Me"),
    subject="????",
    text_body=text,
    html_body=html
)

message.send('smtp.googlemail.com', login=creds['email_username'],
password = creds['email_password'], tls=True)
