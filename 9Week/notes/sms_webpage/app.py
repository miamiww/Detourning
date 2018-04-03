from flask import Flask, request, render_template
import sms

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template("sms.html")
    else:
        message = request.form.get('death_threat', '')
        sms.send_text(message)
        return 'Thanks, you sent "' + message + '"'
