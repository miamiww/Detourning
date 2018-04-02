import requests
from bs4 import BeautifulSoup
# import random
from twilio.rest import Client
import json


url = "https://smittenkitchen.com/?random"

def get_url():
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('h1.entry-title')[0].text
    ref_url = soup.select('h1.entry-title')[0].a['href']
    return title + '\n' + ref_url

with open('creds.json', 'r') as infile:
    creds = json.load(infile)


sid = creds['twilio_sid']
token = creds['twilio_token']

client = Client(sid, token)
numbers = [#'+14152382494','+19175156779','+13107390178',
'+15615989709','+19495005969']

text = get_url()
for number in numbers:
    message = client.messages.create(
     to=number,
     from_='+13472464454',
     body=text
)
