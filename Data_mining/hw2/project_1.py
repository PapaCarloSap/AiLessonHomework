# !pip install pymongo
# !pip install beautifulsoup4
# !pip install lxml

import requests
import bs4
from urllib.parse import urljoin
import pymongo
import datetime
import re


class MagnitParse:
    def __init__(self, start_url, mongo_db):
        self.start_url = start_url
        self.db = mongo_db
    
    def __get_soup(self, url) -> bs4.BeautifulSoup:
        # todo предусмотреть внештатные ситуации
        response = requests.get(url)
        return bs4.BeautifulSoup(response.text, 'lxml')
    
    def run(self):
        for product in self.parse():
            self._save(product)
    
    def parse(self):
        soup = self.__get_soup(self.start_url)
        catalog_main = soup.find('div', attrs={'class': 'сatalogue__main'})
        for product_tag in catalog_main.find_all('a', recursive=False):
            product_name = self._get_name(product_tag)
            if product_name==None:
                continue
            print(product_name)
            yield self.product_parse(product_tag, product_name)
            
    def product_parse(self, product: bs4.Tag, product_name:str) -> dict:
        product = {
            'url': urljoin(self.start_url, product.get('href')),
            'promo_name': self._get_promo(product),
            'product_name': product_name,
            'old_price': self._get_old_price(product),
            'new_price': self._get_new_price(product),
            'image_url': self._get_image_url(product),
            'date_from': self._get_date_from(product),
            'date_to': self._get_date_to(product),
        }
        return product

    def _get_name(self, product:bs4.Tag) -> str:
        content =product.find('div', attrs={'class': 'card-sale__title'})
        if content==None:
            return None
        return content.text

    def _get_image_url(self, product:bs4.Tag) -> str:
        content = product.find('img', attrs={'class': 'lazy'})
        if content==None:
            return None
        return urljoin(self.start_url, content['data-src'])

    def _get_promo(self, product:bs4.Tag) -> str:
        content = product.find('div', attrs={'class': 'card-sale__header'})
        if content==None:
            return None
        return content.text

    def _get_date_from(self, product:bs4.Tag)->datetime:
        content = product.find('div', attrs={'class': 'card-sale__date'}).find_all('p')
        return self._get_date(content[0].text)

    def _get_date_to(self, product:bs4.Tag)->datetime:
        content = product.find('div', attrs={'class': 'card-sale__date'}).find_all('p')
        date_from:datetime =  self._get_date(content[0].text)
        if len(content)<=1:
            return None
        date:datetime = self._get_date(content[1].text)
        if date_from>date:
            return date.replace(year=datetime.date.today().year+1)
        return date

    def _get_date(self, content:str)->datetime:
        raw_data = re.split(r' ', content)
        return datetime.datetime(
            datetime.date.today().year, 
            self._monthToNum(raw_data[2]),
            int(raw_data[1])
            )

    def _get_old_price(self, product: bs4.Tag)->float:
        old_price = product.find('div', attrs={'class': 'label__price_old'})
        if old_price == None:
            return None
        else:
            return self._get_price(old_price)

    def _get_new_price(self, product: bs4.Tag)->float:
        new_price = product.find('div', attrs={'class': 'label__price label__price_new'})
        if new_price == None:
            return None
        else:
            return self._get_price(new_price)

    def _get_price(self, price:bs4.Tag)->float:
        price_rub = price.find('span', attrs={'class': 'label__price-integer'})
        price_penny = price.find('span', attrs={'class': 'label__price-decimal'})
        if price_rub == None or price_penny == None :
            return None
        return float(
            '{0}.{1}'.format(
                price_penny.text, 
                price_penny.text))

    def _save(self, data):
        collection = self.db['magnit']
        collection.insert_one(data)

    def _monthToNum(self, shortMonth):
        return {
                'января' : 1,
                'февраля' : 2,
                'марта' : 3,
                'апреля' : 4,
                'мая' : 5,
                'июня' : 6,
                'июля' : 7,
                'августа' : 8,
                'сентября' : 9, 
                'октября' : 10,
                'ноября' : 11,
                'декабря' : 12
        }[shortMonth]

if __name__ == '__main__':
    database = pymongo.MongoClient('mongodb://alex:x2Z2aX6rYdWAMm@192.168.2.58:27017/')['magnint_promo']
    parser = MagnitParse("https://magnit.ru/promo/?geo=moskva", database)
    parser.run()