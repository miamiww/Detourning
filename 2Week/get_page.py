#import modules
import requests
from bs4 import BeautifulSoup

url = "https://newyork.craigslist.org/d/barter/search/bar"


def get_page(s):
    response = requests.get(url, params={'s': s})
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    links = soup.select('a')
    titles = soup.select('.result-title')
    for title in titles:
        print title.string.strip().encode("utf-8")

#for link in links:
#    print link.string
#    print link.get("href")
get_page(0)
