import scrapy
from urllib.parse import urljoin
from scrapy.http import HtmlResponse
import re
import Data_mining.helper.conv_url as prs
import base64
from termcolor import cprint
import pymongo


url = 'https://auto.youla.ru/'

class AutoyoulaSpider(scrapy.Spider):
    name = 'autoyoula'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['https://auto.youla.ru/']
    user_url='https://youla.ru/'
    db = None

    css_query = {
        "brands": "div.TransportMainFilters_block__3etab a.blackLink",
        "pagination": "div.Paginator_block__2XAPy a.Paginator_button__u1e7D",
        "ads": "article.SerpSnippet_snippet__3O1t2 a[class='SerpSnippet_name__3F7Yu SerpSnippet_titleText__1Ex8A blackLink']",
    }
 
    data_query = {
        "title": lambda resp: resp.css("div.AdvertCard_advertTitle__1S1Ak::text").get(),
        "price": lambda resp: float(resp.css('div.AdvertCard_price__3dDCr::text').get().replace("\u2009", '')),
        "images": lambda resp: resp.css('section.PhotoGallery_thumbnails__3-1Ob button::attr(style)').re('(https?://[^\s]+)\)'),
        'specifications': lambda resp: AutoyoulaSpider.specifications_parse(resp),
        'describe': lambda resp: resp.css("div.AdvertCard_descriptionWrap__17EU3 div.AdvertCard_descriptionInner__KnuRi::text").get(),
        'author': lambda resp: AutoyoulaSpider._parse_autor(resp),
        'mobile': lambda resp: AutoyoulaSpider._parse_phone(resp),
    }

    def __init__(self):
        self.db = pymongo.MongoClient('mongodb://alex:x2Z2aX6rYdWAMm@192.168.2.58:27017/')['jula_promo']

    def parse(self, response, **kwargs):
        brands_links = response.css(self.css_query["brands"])
        yield from self.gen_task(response, brands_links, self.brand_parse)
 
    def brand_parse(self, response):
        pagination_links = response.css(self.css_query["pagination"])
        yield from self.gen_task(response, pagination_links, self.brand_parse)
        ads_links = response.css(self.css_query["ads"])
        yield from self.gen_task(response, ads_links, self.ads_parse)
 
    def ads_parse(self, response):
        data = {}
        for key, selector in self.data_query.items():
            try:
                data[key] = selector(response)
            except (ValueError, AttributeError):
                cprint(f'{key} no parse', 'red')
                continue
        if self.db != None:
            self._save(data)

    def _save(self, data):
        collection = self.db['jula']
        collection.insert_one(data)

    @staticmethod
    def _get_script_content(response:HtmlResponse)->dict:
        for resp_script in response.css("script"):
            find_content_script= re.search(r'(?<=<script>window.transitState = decodeURIComponent\(").*(?="\);</script>)', resp_script.get())
            if find_content_script == None:
                continue
            res = find_content_script.group(0)
            decoder_uri = prs.DecodeURIComponent(res)
            return decoder_uri.to_dict()

    @staticmethod
    def _parse_phone(response:HtmlResponse)->str:
        script_dict = AutoyoulaSpider._get_script_content(response)
        phone = base64.b64decode(script_dict['~#iM']['advertCard']['^0']['contacts']['^0']['phones']['^1'][0]['^0']['phone'])
        phone = base64.b64decode(phone)
        return phone.decode('ascii')

    @staticmethod
    def _parse_autor(response:HtmlResponse)->str:
        script_dict = AutoyoulaSpider._get_script_content(response)
        profile = script_dict['~#iM']['advertCard']['^0']['youlaProfile']
        if profile!=None:
            return urljoin(AutoyoulaSpider.user_url, 'user/{0}'.format(profile['^0']['youlaId']))
        else:
            return urljoin(AutoyoulaSpider.start_urls[0], script_dict['~#iM']['advertCard']['^0']['sellerLink'])

    @staticmethod
    def specifications_parse(response):
        data={}
        for name, value in zip(response.css('div.AdvertCard_specs__2FEHc div.AdvertSpecs_label__2JHnS::text'), 
                                response.css('div.AdvertCard_specs__2FEHc div.AdvertSpecs_data__xK2Qx::text, div.AdvertCard_specs__2FEHc a::text')):
            data[name.get()] = value.get()
        return data
 
    @staticmethod
    def gen_task(response, link_list, callback):
        for link in link_list:
            yield response.follow(link.attrib["href"], callback=callback)
