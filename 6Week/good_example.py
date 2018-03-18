import subprocess
import requests
import random
import os
from bs4 import BeautifulSoup
from vidpy import Clip, Composition

# vid_url = 'https://www.youtube.com/watch?v=qeUM1WDoOGY'

html = requests.get('http://www.foxnews.com').text
soup = BeautifulSoup(html, 'html.parser')

video_links = soup.select('.collection-clips .title a')

link = random.choice(video_links)
vid_url = link.get('href')
print vid_url

subprocess.call(['youtube-dl', vid_url, '-o', 'videos/lolfox.flv'])

clip = Clip('videos/lolfox.flv')
clip.spin(5)

clip.preview()
# Compositions([clip]).save('videos/spinnylol.mp4')

os.remove('videos/lolfox.flv')
