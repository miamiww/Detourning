import requests
from bs4 import BeautifulSoup
import random
import os
from textblob import TextBlob
from vidpy import Clip, Text, Composition

def download_file(url, local_filename=None):
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


def get_random_question():
    html = requests.get("https://answers.yahoo.com/answer").text
    soup = BeautifulSoup(html, 'html.parser')
    questions = soup.select('.qHead a')
    question = random.choice(questions).text
    return question

def search_questions(q):
    html = requests.get('https://answers.search.yahoo.com/search?fr=uh3_answers_web_gs&p=' + q).text
    soup = BeautifulSoup(html, 'html.parser')
    questions = soup.select('h3.title')
    question = random.choice(questions).text
    return question

def get_nouns(text):
    blob = TextBlob(text)
    nouns = []
    for word in blob.tags:
        if word[1] == 'NN' or word[1] == 'NNS':
            nouns.append(word[0])
    return nouns

def get_image(word):
    url = "http://shutterstock.com/search?search_source=base_landing_page&searchterm=" + word
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    image = random.choice(soup.select('.img-wrap img'))
    url = 'https:' + image.get('src')
    return download_file(url)

def make_video():
    randomq = get_random_question()
    nouns = get_nouns(randomq)
    print randomq
    print nouns
    saved_image = get_image(random.choice(nouns))
    print saved_image
    clip = Clip(saved_image, start=0, end=2)
    text = Text(randomq, start=0, end=2)
    text.spin(20)
    comp = Composition([clip,text])
    comp.save('lol.mp4')
# randomq = get_random_question()
# print randomq
