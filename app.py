from bs4 import BeautifulSoup as bs
import os
from flask import Flask, jsonify, request, url_for, redirect, render_template, session
from pymongo import mongo_client
from collections import defaultdict
import json
from pyreqs import objectHandler
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ronin-Rock'
paloulr = 'https://www.prothomalo.com/api/v1/collections/{}?limit={}&fields=headline,url,cards,alternative'
bbcurl = 'https://www.bbc.com/bengali/mostread.json'

catdict = {'TECH': 'technology', 'LATEST': 'latest',
           'BD': 'bangladesh'}


@app.route('/home', methods=['GET'])
def homer():
    print('in home')
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/selector', methods=['POST', 'GET'])
def selector():
    if request.method == 'POST':
        print('in selector!!!!!!!')
        data = request.get_json()
        # print(data['npaper'])
        npaper = data['npaper']
        catagoty = data['catagoty']

    return render_template('home.html')


@app.route('/<news>/<cat>')
def index(cat, news):
    if news == 'palo':
        response = requests.get(paloulr.format(catdict[cat], 12))
        jsonResponse = response.json()
        print("Entire JSON response")
        jsonlst = jsonResponse['items']
    if news == 'bbc':
        response = requests.get(bbcurl)
        jsonResponse = response.json()

        jsonlst = jsonResponse['records']
        # return jsonResponse

    # file = open('./kett.json', 'r', encoding="utf8")
    # f = file.read()
    # objs = json.loads(f)
    # file.close()

    objs = objectHandler.newsmaker(jsonlst, paper=news)

    # world = objectHandler.newsmaker(objs)
    # print(len(world))
    # print(xx)
    print(len(objs))

    return render_template('index.html', newsls=objs, catg=cat.upper())


if __name__ == '__main__':

    app.run(debug=True)
