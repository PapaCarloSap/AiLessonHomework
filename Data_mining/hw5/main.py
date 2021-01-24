from scrapy import crawler
from scrapy import settings
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from Data_mining.hw5.gb_parse.spiders.autoyoula import AutoyoulaSpider
from Data_mining.hw5.gb_parse.spiders.headhunter import HeadhunterSpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule('gb_parse.settings')
    crawler_process = CrawlerProcess(settings=crawler_settings)
    #crawler_process.crawl(AutoyoulaSpider)
    crawler_process.crawl(HeadhunterSpider)
    crawler_process.start()