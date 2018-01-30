#import modules
import requests
from bs4 import BeautifulSoup
import time

url = "https://newyork.craigslist.org/d/wanted/search/waa"

headers = {'content-type': 'application/json'}

def get_page(s):
    response = requests.get(url, params={'s': s})
    html = response.text
    soup = BeautifulSoup(html,"html.parser", headers=headers)
    links = soup.select('a')
    titles = soup.select('.result-title')

    output = []
    for title in titles:
        clean_title = title.text.strip().encode('utf-8')
        output.append(clean_title)
    return output

start = 0
while start < 2500:
    results = get_page(start)
    for r in results:
        print r
    time.sleep(0.5)
    start = start + 120
