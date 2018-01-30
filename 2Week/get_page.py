#import modules
import requests
from bs4 import BeautifulSoup

url = "https://newyork.craigslist.org/d/barter/search/bar"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html)
links = soup.select('a')

#for link in links:
#    print link.string
#    print link.get("href")

titles = soup.select('.result-title')

for title in titles:
    print title.string.strip().encode("utf-8")
