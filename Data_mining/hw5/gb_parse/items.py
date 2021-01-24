# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GbParseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class AutoyoulaItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    images = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    specifications = scrapy.Field()
    price = scrapy.Field()
    test = scrapy.Field()

class HeadHunterVacancyItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    description = scrapy.Field()
    skills = scrapy.Field()
    author = scrapy.Field()

class HeadHunterAuthorItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
