import glob
from PIL import Image
import os
import time
import requests
from selenium import webdriver
import subprocess

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/samlavigne/')

def DownloadFile(url, local_filename=None):
#from: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    if local_filename is None:
        local_filename = url.split('/')[-1]

    if os.path.exists(local_filename):
        return local_filename

    # if not url.startswith('http:'):
    #     url = 'http:' + url

    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

for x in range(0,10):
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

images = driver.find_elements_by_css_selector('img')


for i, image in enumerate(images):
    url = image.get_attribute('src')
    savedname = 'mypics/' + str(i) + '.jpg'
    DownloadFile(url,savedname)


driver.quit()

blank_image = Image.new('RGB', (500,500), (255,255,255))

x=0
y=0

jpegs = glob.glob('mypics/*.jpg')
for jpg in jpegs:
    im = Image.open(jpg)
    im.thumbnail((101,101))
    width = im.size[0]
    height = im.size[1]
    # x = random.randint(0,500)
    # y = random.randint(0,500)
    blank_image.paste(im,(x,y))
    x = x+width
    if x > 500:
        x = 0
        y = y+height

blank_image.save('bigbaby.jpg')
supprocess.call(['convert','mypics/*.jpg','myfeed.gif'])
