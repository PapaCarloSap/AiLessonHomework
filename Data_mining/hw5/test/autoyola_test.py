from scrapy.http import HtmlResponse
from Data_mining.hw5.gb_parse.spiders.autoyoula import AutoyoulaSpider
import requests


headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
    }

def test_ads_parse():
    url = "https://auto.youla.ru/advert/used/brilliance/h530/prv--390d963822da2ff5/"
    r = requests.get(url, headers=headers)
    response = HtmlResponse(url=url, body=r.text, encoding='utf-8')
    #response = (url)
    
    target = AutoyoulaSpider()
    target.ads_parse(response)

def test_parse_autor():
    url = 'https://auto.youla.ru/advert/used/audi/a6/prv--72f5e577aee5e96d/'
    r = requests.get(url, headers=headers)
    response = HtmlResponse(url=url, body=r.text, encoding='utf-8')
    assert AutoyoulaSpider._parse_autor(response) == 'https://youla.ru/user/5b8285d9821a99a64f0b2dc2'

def test_parse_autor_2():
    url = 'https://auto.youla.ru/advert/used/uaz/pickup/avs-tsentr-prodag-avto-s-probegom-rrt-avtomarket--70a327f10bb339fb/'
    r = requests.get(url, headers=headers)
    response = HtmlResponse(url=url, body=r.text, encoding='utf-8')
    assert AutoyoulaSpider._parse_autor(response) == 'https://auto.youla.ru/cardealers/salon-tsentr-prodag-avto-s-probegom-rrt-avtomarket-9531/'

def test_parse_phone():
    url = 'https://auto.youla.ru/advert/used/audi/a6/prv--72f5e577aee5e96d/'
    r = requests.get(url, headers=headers)
    response = HtmlResponse(url=url, body=r.text, encoding='utf-8')
    assert AutoyoulaSpider._parse_phone(response) == '+7 (981) 426-18-86'