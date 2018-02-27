import requests
import os
from bs4 import BeautifulSoup

url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"
response = requests.get(url)
#
# with open('cat.jpg', 'wb') as outfile:
#     outfile.write(response.content)



def DownloadFile(url, local_filename=None):
#from: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
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

# DownloadFile(url)

def get_shutterstock_images(q):
    url = 'https://www.shutterstock.com/search'
    params = {'searchterm':q}
    html = requests.get(url, params=params).text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select('.img-wrap img')

    for image in images:
        img_url = 'https:' + image.get('src')
        # print image.get('src')
        print img_url
        DownloadFile(img_url)

def get_images(url):
    html=requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    images = soup.select('img')
    for image in images:
        img_url = image.get('src')
        try:
            DownloadFile(img_url)
        except:
            continue

get_images('http://rcpp.lensbased.net/')
