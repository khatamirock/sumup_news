from bs4 import BeautifulSoup as bs
import os
from flask import Flask, jsonify, request, url_for, redirect, render_template, session
from pymongo import mongo_client
from collections import defaultdict
import json
from pyreqs import objectHandler
import requests
# from !!rock
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ronin-Rock'
paloulr = 'https://www.prothomalo.com/api/v1/collections/{}?limit={}&fields=headline,url,cards,alternative'
bdnwsurl = 'https://bangla.bdnews24.com/api/v1/collections/{}?limit={}&fields=headline,url,cards,hero-image-s3-key'

bbcurl = 'https://www.bbc.com/bengali/mostread.json'
# palo world update->> https://www.prothomalo.com/api/v1/collections/world-rest15?limit=10&fields=headline,url,cards,alternative
# https://bangla.bdnews24.com/api/v1/collections/105128?limit=8&fields=headline
#                                             105128->>বাণিজ্য
#                                               105129->>খেলা
#                                               105130->>বিনোদন
#                                               105131->>বিশ্ব
#                                               105132->>বাংলাদেশ
#                                               105133->>স্বাস্থ্য
#                                               105134->>প্রবাস
#                                               105135->>প্রযুক্তি
#                                               105136->>লাইফস্টাইল
#                                               105137->>বিজ্ঞান
#                                               105138->>সাহিত্য
#                                               105139->>কলাম
#                                               105140->>বিশেষ প্রতিবেদন
#                                               105141->>সাম্প্রতিক খবর
#                                               105142->>সাম্প্রতিক সংবাদ

# https://bangla.bdnews24.com/api/v1/collections/110199?limit=8&fields=headline


pcatdict = {'TECH': 'technology', 'LATEST': 'latest',
            'BD': 'bangladesh',
            'WORLD': 'world-rest15'
            }


bdcatdict = {'TECH': '109765', 'LATEST': '109765',
             'BD': '109765',
             'WORLD': 'world-grid'
             }


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
        response = requests.get(paloulr.format(pcatdict[cat], 12))
        jsonResponse = response.json()
        print("Entire JSON response")
        jsonlst = jsonResponse['items']

    if news == 'bdn':

        response = requests.get(bdnwsurl.format(bdcatdict[cat], 9))
        jsonResponse = response.json()
        print("Entire JSON response")
        jsonlst = jsonResponse['items']

    if news == 'bbc':
        response = requests.get(bbcurl)
        jsonResponse = response.json()

        jsonlst = jsonResponse['records']

    objs = objectHandler.newsmaker(jsonlst, news)

    return render_template('index.html', newsls=objs, catg=cat.upper(), newsname=news)


if __name__ == '__main__':

    app.run(debug=True)
