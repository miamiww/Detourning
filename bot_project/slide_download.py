import requests
from bs4 import BeautifulSoup
import random
import os
# from textblob import TextBlob
# from vidpy import Clip, Text, Composition

base_url = "https://www.slideshare.net/"

def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]

    if os.path.exists(local_filename):
        return local_filename

    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def get_slide(source):
    url = base_url + source
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    image = random.choice(soup.select('.slide_image div.slide.show'))
    url = image.get('src')
    return download_file(url)
