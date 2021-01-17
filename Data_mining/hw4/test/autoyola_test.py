from scrapy.http import HtmlResponse
from Data_mining.hw4.gb_parse.spiders.autoyoula import AutoyoulaSpider
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