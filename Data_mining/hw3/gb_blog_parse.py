import os
import requests
import bs4
from urllib.parse import urljoin
# from dotenv import load_dotenv
from Data_mining.hw3.database import Database

class GbParse:
    home_url='https://geekbrains.ru/'
    post_url= '{}/posts'.format(home_url)

    def __init__(self):
        self.tasks = []
        self.done_urls = set()

    def _get_site_content(self, *args, **kwargs) -> bs4.BeautifulSoup:
        response = requests.get(*args, **kwargs)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        return soup

    def _page_parse(self, url, page:bs4.BeautifulSoup) -> dict:
        gb_pagination:bs4.PageElement = page.find('ul', attrs={'class': 'gb__pagination'})
        page_a_tags = gb_pagination.find_all('a')
        for page_a in page_a_tags:
            page_url=urljoin(url, page_a.get('href'))
            if page_url not in self.done_urls:
                task = self._parse_task(page_url, self._page_parse)
                self.tasks.append(task)
                self.done_urls.add(page_url)

        post_urls = page.find_all('a', attrs={'class': 'post-item__title'})
        for post_url in post_urls:
            post_href = urljoin(url, post_url.get('href'))
            if post_href not in self.done_urls:
                task = self._parse_task(post_href, self._post_parse)
                self.tasks.append(task)
                self.done_urls.add(post_url)

    def _parse_task(self, url, callback):
        def wrap():
            content = self._get_site_content(url)
            return callback(url, content)
        return wrap

    def _post_parse(self, url, post) -> dict:
        author_name_tag = post.find('div', attrs={'itemprop': 'author'})
        data = {
            'post_data': {
                'url': url,
                'title': post.find('h1', attrs={'class': 'blogpost-title'}).text,
            },
            'author': {
                'url': urljoin(url, author_name_tag.parent.get('href')),
                'name': author_name_tag.text,
            },
            'tags': [{
                'name': tag.text,
                'url': urljoin(url, tag.get('href')),
            } for tag in post.find_all('a', attrs={'class': 'small'})],
        }
        return data

    def parse_blogs_to(self, database:Database):
        #  reset
        self.tasks.clear()
        self.tasks.append(self._parse_task(self.post_url, self._page_parse))
        self.done_urls.clear()
        self.done_urls.add(self.post_url)
        # start parse
        for task in self.tasks:
            result = task()
            if result:
                database.create_post(result)

if __name__ == '__main__':
    parser = GbParse()
    parser.parse_blogs_to(Database(os.environ['SQLITE_DBURL']))