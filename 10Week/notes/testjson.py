import json
import sys
import requests
from bs4 import BeautifulSoup

# data = [
#     {"job": "foot scribber", "salary": "$500,000"},
#     {"job": "ruthless capitalist", "salary": "$15"}
# ]

def get_description(query):
    url = "https://www.shutterstock.com/search?searchterm=" + query
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    out = []
    images = soup.select(".img-wrap img")
    for image in images:
        item = {
            "source": image.get('src'),
            "description": image.get('alt')
        }
        out.append(item)
    return(out)

data = get_description(sys.argv[1])

with open("data.json", "w") as infile:
    json.dump(data, infile, indent=2)
