import requests
import os
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter, ImageDraw, ImageFont

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

def write_text(imgfilename, ttle):
    im = Image.open(imgfilename)
    canvas = ImageDraw.Draw(im)
    canvas.rectangle([0,125,im.size[0], 170], fill=(0,0,0))
    fnt = ImageFont.truetype('/Library/Fonts/Brush Script.ttf', 40)
    canvas.text( (10,125), ttle, font=fnt, fill=(255,255,255))
    im.save(imgfilename + '.modified.jpg')

def get_shutterstock_images(q):
    url = 'https://www.shutterstock.com/search'
    params = {'searchterm':q}
    html = requests.get(url, params=params).text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select('.img-wrap img')

    for image in images[0:10]:#images:
        img_url = 'https:' + image.get('src')
        # print image.get('src')
        title = image.get('alt')
        print img_url
        filename = DownloadFile(img_url)
        write_text(filename, 'gimme da gorbage')

get_shutterstock_images('cats')
