from bs4 import BeautifulSoup as bs
import os
from flask import Flask, jsonify, request, url_for, redirect, render_template, session
from pymongo import mongo_client
from collections import defaultdict
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'robret-kohler'


@app.route('/<name>')
def name(name):
    return '''
    <div style="text-align: center;">
    <h2 style="display:block">Hello <h1 style="">{}!</h1></h2>
       <p> here are some instructions .........</br>
        1.get the browser open and install the postMan request plugin-CHrome</br>
        2. go to the link below and make a potr request</br>
        3. make sure that the request body is in json format</br>
        4. ex: =>> "doc":"YOUR sent............","ratio":sent_number_in _intger </p>
         </div>
        '''.format(name)


@app.route('/')
def index():

    file = open('./kett.json', 'r', encoding="utf8")
    f = file.read()
    objs = json.loads(f)

    file.close()
    return render_template('index.html', newsls=objs)


if __name__ == '__main__':

    app.run(debug=True)
