import time
import json
import requests
import os
import os.path

class StatusCodeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Parser5ka:
    
    home_url='https://5ka.ru/'
    file_category_url='api/v2/categories/'
    category_url = home_url + file_category_url
    products_by_category_url= home_url + 'api/v2/special_offers/?store=&records_per_page=12&page=1&categories={0}'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
    }
    
    def __init__(self):
        self.repo_path = os.path.join(os.path.dirname(__file__), '__tmp__')
        os.makedirs(self.repo_path, exist_ok=True)
    
    def load_products_by_category(self):
        for category in self._parse_categories(self.category_url):
            for product in self._parse_products(self._get_url_products_by_category(category['parent_group_code'])):
                category_name = category['parent_group_name'].replace(' ', '_')
                file_path = os.path.join(self.repo_path, f'{category_name}.json')
                self.save_file(file_path, product)
    
    def _parse_categories(self, url):
        response = self._get_response(url, headers=self.headers)
        data: dict = response.json()
        for category_info in data:
            yield category_info

    def _parse_products(self, url):
        while url:
            response = self._get_response(url, headers=self.headers)
            data: dict = response.json()
            url = data['next']
            yield data.get('results', [])

    def _get_url_category(self, category_code: str) -> str:
        return self.category_url + category_code + '/'

    def _get_url_products_by_category(self, category_code: str) -> str:
        return self.products_by_category_url.format(category_code)

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
    
    def save_file(self, file_path, data: dict):
        with open(file_path, 'w', encoding='UTF-8') as file:
            # file.write(json.dumps(data))
            json.dump(data, file, ensure_ascii=False)


if __name__ == '__main__':
    parser = Parser5ka()
    parser.load_products_by_category()