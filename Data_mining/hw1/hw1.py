import time
import json
from pathlib import Path
import requests

class StatusCodeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Parser5ka:
    
    home_url='https://5ka.ru/'
    file_category_url='api/v2/categories/'
    category_url = home_url + file_category_url
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
    }
    
    def __init__(self):
        pass
    
    def load_products_by_category(self):
        for category in self._parse_categories(self.category_url):
            for product in self._parse_products(self._get_url_category(category['parent_group_code'])):
                pass

        for products in self.parse(self.start_url):
            for product in products:
                file_path = Path(__file__).parent.joinpath(f'{product["id"]}.json')
                self.save_file(file_path, product)
    
    def _parse_categories(self, url):
        response = self._get_response(url, headers=self.headers)
        data: dict = response.json()
        for category_info in data:
            yield category_info
            # url = data['next']
            # for category_info in data:
            #     for category in self._parse_categories(self._get_url_category(category_info['parent_group_code'])):
            #         pass
            #         #yield _parse_categories(_get_url_category(category['parent_group_code']))
            # yield data.get('results', [])

    def _parse_products(self, url):
        pass

    def _get_url_category(self, category_code: str) -> str:
        return self._parse_categories + category_code + '/'

    def _get_response(self, url, **kwargs):
        while True:
            try:
                response = requests.get(url, **kwargs)
                if response.status_code != 200:
                    raise StatusCodeError(f'status {response.status_code}')
                return response
            except (requests.exceptions.ConnectTimeout,
                    StatusCodeError):
                time.sleep(0.1)
    
    def parse(self, url):
        while url:
            response = self._get_response(url, headers=self.headers)
            data: dict = response.json()
            url = data['next']
            yield data.get('results', [])
    
    def save_file(self, file_path: Path, data: dict):
        with open(file_path, 'w', encoding='UTF-8') as file:
            # file.write(json.dumps(data))
            json.dump(data, file, ensure_ascii=False)


if __name__ == '__main__':
    parser = Parser5ka('https://5ka.ru/api/v2/categories/')
    parser.load_products_by_category()