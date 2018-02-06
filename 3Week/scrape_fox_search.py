import requests

url = 'http://api.foxnews.com/v1/content/search?q=lol&fields=date,description,title,url,image,type,taxonomy&section.path=fnc&start=0'
#delete callbacks part of url

results = requests.get(url).json()
docs = results['response']['docs']
for doc in docs:
    print doc['title']
