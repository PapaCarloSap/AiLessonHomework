import scrapy
from urllib.parse import urljoin


url = 'https://auto.youla.ru/'

class AutoyoulaSpider(scrapy.Spider):
    name = 'autoyoula'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['https://auto.youla.ru/']

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
        # 'author': '',#lambda resp: urljoin(url, resp.css("div.SellerInfo_block__1HmkE a.SellerInfo_name__3Iz2N::attr(href)").get()),
        # 'mobile': '',
    }

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
                continue
        print(data)

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
