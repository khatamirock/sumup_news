
from pyreqs.summarizer import *

from json_extract import GetValue2
import re
regex = re.compile(r'<[^>]+>')


class bdnews:
    def __init__(self, objs):
        
        
        self.title = objs['story']['headline']
        #
        try:
            self.image ="https://gumlet.assettype.com/" +  objs['story']['hero-image-s3-key']
        except:
            self.image = '\static\image\defl.jpg'
        # news having multiple ['story-elements'] objects;;;;
        self.news = self.newsmake(objs['story']['cards']).replace(
            '\'', '').replace(']', '').replace('[', '')
        self.newsurl = objs['story']['url']
        self.rawlen
        self.sumlen
        self.percent

        # self.image = "https://gumlet.assettype.com/" + \
        #     objs['story']['hero-image-s3-key']
    def newsmake(self, cards):
        news = ''
        for card in cards:
            getobj = GetValue2(card)
            # print('\n\n\n', cards)
            news += str(getobj.get_values("text", deep=True))
            # print(xs)
        DOCUMENT = cleanText(news)
        # print(DOCUMENT)
        rawlen = sum(len(nw.split()) for nw in news)

        similarity_matrix = getSimmat(DOCUMENT)

        scores = run_page_rank(similarity_matrix)
        news = get_top_sentences(scores, DOCUMENT, int(3))
        sumlen = sum(len(nw.split()) for nw in news)
        self.rawlen = rawlen
        self.sumlen = sumlen
        self.percent = int(((rawlen-sumlen)/rawlen)*100)

        return regex.sub('', news)


class bbcNews:
    def __init__(self, objs):
        try:
            self.title = objs['promo']['headlines']['seoHeadline']
        except:
            pass
        #
        try:
            self.image = 'https://ichef.bbci.co.uk/news/640/cpsprodpb/' + \
                objs['promo']['images']['defaultPromoImage']['blocks'][3]['locator']
        except:
            self.image = '\static\image\defl.jpg'

        self.news = 'NEWS FORMAT NOT FOUND !!!!!!!!!!!!'
        self.newsurl = objs['promo']['locators']
        # self.rawlen
        # self.sumlen
        self.percent = 0




regex = re.compile(r'<[^>]+>')

class paloNews:
    def __init__(self, objs):
        print(len(objs))
        
        story = objs.get('story')
        if story is None:
            self.title = 'Default Title'
            self.image = '\static\image\defl.jpg'
            self.news = 'No news available'
            self.newsurl = ''
            self.rawlen = 0
            self.sumlen = 0
            self.percent = 0
        else:
            self.title = story.get('headline', 'Default Title')
            try:
                self.image = story.get('alternative', {}).get('home', {}).get('default', {}).get('hero-image', {}).get('hero-image-url', '\static\image\defl.jpg')
            except:
                self.image = '\static\image\defl.jpg'
            self.news = self.newsmake(story.get('cards', [])).replace('\'', '').replace(']', '').replace('[', '')
            self.newsurl = story.get('url', '')
    
    def newsmake(self, cards):
        news = ''
        for card in cards:
            getobj = GetValue2(card)
            news += str(getobj.get_values("text", deep=True))
        DOCUMENT = cleanText(news)
        rawlen = sum(len(nw.split()) for nw in news)

        similarity_matrix = getSimmat(DOCUMENT)
        scores = run_page_rank(similarity_matrix)
        news = get_top_sentences(scores, DOCUMENT, int(3))
        sumlen = sum(len(nw.split()) for nw in news)
        self.rawlen = rawlen
        self.sumlen = sumlen
        self.percent = int(((rawlen - sumlen) / rawlen) * 100)

        return regex.sub('', news)

# Other classes remain unchanged

def newsmaker(lsts, paper):
    newsObjs = []
    if paper == 'palo':
        for news in lsts[1:]:
            newsObjs.append(paloNews(news))
    elif paper == 'bdn':
        for news in lsts:
            newsObjs.append(bdnews(news))
    elif paper == 'bbc':
        for news in lsts:
            newsObjs.append(bbcNews(news))
    return newsObjs