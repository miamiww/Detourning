import glob
from PIL import Image
import os
import time
import requests
from selenium import webdriver
import subprocess
from bs4 import BeautifulSoup
import sys



def DownloadFile(url, local_filename=None):
#from: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    if local_filename is None:
        local_filename = url.split('/')[-1]

    if os.path.exists(local_filename):
        return local_filename

    if not url.startswith('http'):
        url = 'http:' + url

    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def get_images(url):
    html=requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    images = soup.select('img')
    for i, image in enumerate(images):
        img_url = image.get('src')
        savedname = 'frames/' + str(i) + '.jpg'
        try:
            filename = DownloadFile(img_url,savedname)
        except Exception as e:
            print e
            continue
    subprocess.call(['convert','frames/*.jpg','coolgif.gif'])

# get_images('http://rcpp.lensbased.net/')

get_images(sys.argv[1])
