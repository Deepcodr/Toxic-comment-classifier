from flask import Flask,render_template,request
import json
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/checkcomment", methods=["POST"])
def checkcomment():
    # print(request.form['comment'])
    # print(request.json["comment"])
    cd=request.data.decode('utf8')
    lcd=cd.split('=')
    comment=lcd[1]
    print(comment)
    model=pickle.load(open('model.pkl','rb'))
    
    return "Hello"