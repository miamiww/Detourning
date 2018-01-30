import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.reddit.com/r/Showerthoughts/").text

soup = BeautifulSoup(html)

titles = soup.select('a.title')

for title in titles:
    print title.text.strip()
