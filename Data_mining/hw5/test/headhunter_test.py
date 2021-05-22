from scrapy.http import HtmlResponse
from scrapy.http.request import Request
from Data_mining.hw5.gb_parse.spiders.headhunter import HeadhunterSpider
import requests
import pytest


headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
    }

@pytest.yield_fixture()
def pagination_request():
    url = 'https://hh.ru/search/vacancy?schedule=remote&L_profession_id=0&area=113'
    r = requests.get(url, headers=headers)
    response = HtmlResponse(url=url, body=r.text, encoding='utf-8')
    target = HeadhunterSpider()
    yield from target.parse(response)
    print('all')

def test_nohelper(pagination_request:Request):
    pass
    # result = pagination_request.callback()
    # print(result)

@pytest.yield_fixture()
def vacancy_parse():
    url = 'https://hh.ru/vacancy/41747727'
    r = requests.get(url, headers=headers)
    response = HtmlResponse(url=url, body=r.text, encoding='utf-8')
    yield from HeadhunterSpider()._vacancy_parse(response)

def test_vacancy_parse(vacancy_parse):
    assert True