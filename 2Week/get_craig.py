#import modules
import requests

url = "https://newyork.craigslist.org/d/barter/search/bar"
response = requests.get(url)
html = response.text
print html
