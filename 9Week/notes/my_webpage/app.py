'''
to setup app: export FLASK_APP=app.py
to enable debug: export FLASK_DEBUG=1
to start: flask run
'''

from flask import Flask, request, render_template
import fake_news

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', '')
    return render_template("greetings.html", name=name, insult="dumb")

@app.route('/ghostnews/')
def ghostnews():
    headline = request.args.get('headline','')
    if headline != '':
        imagename = fake_news.realnews_headless(headline)
        return '<img src="/static/{}">'.format(imagename)
    else:
        return 'oops'




@app.route('/bye/')
def bye():
    return "<b>bye !</b>"

@app.route('/greetings/')
def greetings():
    name = request.args.get('name', '')
    insult = request.args.get('insult','nothing')
    return 'hello ' + name + ' you are ' + insult

@app.route('/question/')
def question():
    return render_template('form.html')

@app.route('/doit/', methods=['POST'])
def doit():
    age = request.form.get('age')
    return "You are " + age + " years old"
