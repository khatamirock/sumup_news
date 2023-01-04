
from pyreqs.summarizer import *

from json_extract import GetValue2
import re
regex = re.compile(r'<[^>]+>')


class bdnews:
    def __init__(self, objs):
        self.title = objs['story']['headline']
        #
        try:
            self.image = objs['story']['hero-image-s3-key']
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


class paloNews:
    def __init__(self, objs):
        self.title = objs['story']['headline']
        #
        try:
            self.image = objs['story']['alternative']['home']['default']['hero-image']['hero-image-url']
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


def newsmaker(lsts, paper):
    newsObjs = []
    print('>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n\n\n\n\n>>>>>', paper)
    if paper == 'palo':
        print('paloeee')
        for news in lsts:
            # print(news['story']['headline'])
            newsObjs.append(paloNews(news))
    if paper == 'bdn':
        for news in lsts:
            newsObjs.append(bdnews(news))

    if paper == 'bbc':
        print('BCC')
        for news in lsts:
            newsObjs.append(bbcNews(news))

    return newsObjs
