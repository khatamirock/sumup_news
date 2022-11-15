from selenium import webdriver
from bs4 import BeautifulSoup as bs
from collections import defaultdict
import os
from flask import Flask, jsonify, request, url_for, redirect, render_template, session
import re

from pymongo import mongo_client


def driversetup():
    # pass
    options = webdriver.ChromeOptions()
    # run Selenium in headless mode
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    # overcome limited resource problems
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("lang=en")
    # open Browser in maximized mode
    options.add_argument("start-maximized")
    # disable infobars
    options.add_argument("disable-infobars")
    # disable extension
    # options.add_argument("--disable-extensions")
    # options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

    return driver


driver = driversetup()


def pagesource(url):
    driver.get(url)
    soup = bs(driver.page_source)
    # driver.close()
    return soup


def gettextnews(url):
      # story-grid
    # url1='https://www.prothomalo.com/world/pakistan/mdmgit24p2'
#     driver2 = driversetup()

    xx = pagesource(url)
    xy = xx.select('.story-element-text')
    news = ''
    for x in xy:
        news += x.text
    return news


url='https://bangla.bdnews24.com/samagrabangladesh'

xx = pagesource(url)


# # NFUuA
lists=xx.select('.arr--story-card a')
# # print(lists)
# print(len(lists))
# for ls in lists[:6]:
#   print(ls)


newsdict=defaultdict(list)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
for l in range(0,len(lists),2):
  l1=lists[l]
  l2=lists[l+1]
  link=l1['href']
  # print(l)
  try:
    imaglink=l1.select('img')[0]['data-src']
  except:
    imaglink='null'
  # print(imaglink,'\n',l2.text)
  newsdict[l2.text].append(link)
  newsdict[l2.text].append(imaglink)
  



print(len(newsdict))
print(newsdict)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'robret-kohler'


@app.route('/<name>')
def name(name):
    return '''
    <div style="text-align: center;">
    <h2 style="display:block">Hello <h1 style="">{}!</h1></h2>
       <p> here are some instructions .........</br>
        1.get the browser open and install the postMan request plugin-CHrome</br>
        2. go to the link below and make a post request</br>
        3. make sure that the request body is in json format</br>
        4. ex: =>> "doc":"YOUR sent............","ratio":sent_number_in _intger </p>
         </div>
        '''.format(name)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True)
