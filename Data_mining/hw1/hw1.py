import time
import json
from pathlib import Path
import requests

"""
GET
POST
PUT
PATCH
DELETE
"""

"""
1xx
2xx
3xx
4xx
5xx
"""

class StatusCodeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Parser5ka:
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0"
    }
    
    def __init__(self, start_url):
        self.start_url = start_url
    
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
    
    def run(self):
        for products in self.parse(self.start_url):
            for product in products:
                file_path = Path(__file__).parent.joinpath(f'{product["id"]}.json')
                self.save_file(file_path, product)
    
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
    parser = Parser5ka('https://5ka.ru/api/v2/special_offers/')
    parser.run()