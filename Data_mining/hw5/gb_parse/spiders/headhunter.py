import scrapy
from ..loaders import HeadHunterVacancyLoader


class HeadhunterSpider(scrapy.Spider):
    name = 'headhunter'
    allowed_domains = ['hh.ru']
    #start_urls = ['https://https://hh.ru/search/vacancy/']
    start_urls = ['https://hh.ru/search/vacancy?schedule=remote&L_profession_id=0&area=113']

    list_vacancy_query = {
        "pagination": "//span[contains(@class, 'bloko-button-group')]//a[@data-qa='pager-page']/@href",
        "vacancy":"//a[@data-qa='vacancy-serp__vacancy-title']/@href"
    }

    vacancy_query = {
        "name": "//h1[@data-qa='vacancy-title']/text()",
        "salary": '//p[@class="vacancy-salary"]/span/text()',
        "description": '//div[@data-qa="vacancy-description" and @class="g-user-content"]//text()',
        "skills": '//div[@class="bloko-tag-list"]//text()',
        "author": '//div[@class="vacancy-company__details"]/a[@data-qa="vacancy-company-name"]/@href'
    }

    def parse(self, response):
        pagination_links = response.xpath(self.list_vacancy_query["pagination"])
        yield from self.gen_task(response, pagination_links, self.parse)
        vacancy_links = response.xpath(self.list_vacancy_query["vacancy"])
        yield from self.gen_task(response, vacancy_links, self._vacancy_parse)
        
    def _vacancy_parse(self, response):
        loader = HeadHunterVacancyLoader(response=response)
        for key, selector in self.vacancy_query.items():
            loader.add_xpath(key, selector)
        loader.add_value('url', response.url)
        item = loader.load_item()
        yield item

    @staticmethod
    def gen_task(response, link_list, callback):
        for link in link_list:
            yield response.follow(link, callback=callback)