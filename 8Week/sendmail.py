from envelopes import Envelope

import json

with open('creds.json', 'r') as infile:
    creds = json.load(infile)


message = Envelope(
    from_addr=("detourning2018@gmail.com", "lol"),
    to_addr=("arj247@nyu.edu", "Me"),
    subject="????",
    text_body="a spectre is haunting your email"
)

message.send('smtp.googlemail.com', login=creds['email_username'],
password = creds[email_password], tls=True)
