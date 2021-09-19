import os
import requests
import bs4
from urllib.parse import urljoin
import re
from Data_mining.hw3.database import Database
from Data_mining.helper.converters import get_date_dd_mon_year, StatusCodeError
import time
from termcolor import cprint

class GbParse:
    home_url='https://geekbrains.ru/'
    post_url= '{}/posts'.format(home_url)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
    }
    not_found= "none"

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
            content = self._get_site_content(url, headers=self.headers)
            return callback(url, content)
        return wrap

    def _post_parse(self, url, post) -> dict:
        print(url)
        title = self._get_title(post)
        cprint(f'{title}', 'green')
        author_name_tag = post.find('div', attrs={'itemprop': 'author'})
        data = {
            'post_data': {
                'url': url,
                'title': title,
                'post_image': self._get_post_image(post),
                'date': get_date_dd_mon_year(self._get_data_content(post)), 
                'num_watch': self._get_num_watch(post)
            },
            'author': {
                'url': urljoin(url, author_name_tag.parent.get('href')),
                'name': self._remove_empty_space(author_name_tag.text),
            },
            'tags': [{
                'name': tag.text,
                'url': urljoin(url, tag.get('href')),
            } for tag in post.find_all('a', attrs={'class': 'small'})],
            'comments': self._get_comments(post.find('comments')['commentable-id']),
            # 'comments':[{
            #     'data_comment_id' : int(comment.find('div', attrs={'class':'gb__comment-item-body'})['data-comment-id']),
            #     'author': {
            #         'url': urljoin(url, comment.find('a', attrs={'class':'gb__comment-item-header-user-data-name'}).get('href')),
            #         'name': comment.find('a', attrs={'class':'gb__comment-item-header-user-data-name'})['creator'],
            #     },
            #     'content': re.search(r'(?<=<p>).*(?=</p>)', comment.find('div', attrs={'class':'gb__comment-item-body-content'})['text']).group(0),
            # } for comment in post.find_all('li', attrs={'class':'gb__comment-item'})],
        }
        return data

    def _get_num_watch(self, post) -> int:
        try:
            return int(post.find_all('span', attrs= {'class': 'text-md'})[1].text)
        except :
            cprint(f'num_watch not found', 'red')
            return 0

    def _get_data_content(self, post):
        try:
            return post.find('time', attrs= {'itemprop': 'datePublished'} ).text
        except :
            cprint(f'date not found', 'red')
            return self.not_found

    def _get_post_image(self, post):
        try:
            return post.find('div', attrs={'class': 'blogpost-content', 'itemprop': 'articleBody'}).p.img.get('src')
        except :
            cprint(f'post_image not found', 'red')
            return self.not_found

    def _get_title(self, post):
        title = post.find('h1', attrs={'class': 'blogpost-title'})
        if title != None:
            return title.text
        else:
            cprint(f'title not found', 'red')
            return self.not_found
    
    def _get_response(self, url, **kwargs):
        while True:
            try:
                print(url)
                response = requests.get(url, **kwargs)
                if response.status_code != 200 and response.status_code != 206: # 206 not all coments readed
                    raise StatusCodeError(f'status {response.status_code}')
                return response
            except (requests.exceptions.ConnectTimeout,
                    StatusCodeError):
                time.sleep(0.1)

    def _get_comments(self, post_id)->dict:
        comments_url = '{0}/api/v2/comments?commentable_type=Post&commentable_id={1}&order=desc'.format(self.home_url, post_id)
        response = self._get_response(comments_url, headers=self.headers)
        comments: dict = response.json()
        result = [{
            'data_comment_id' : int(comment['comment']['id']),
            'author': {
                'url': comment['comment']['user']['url'],
                'name': comment['comment']['user']['full_name'],
            },
            'content': comment['comment']['body'],
        }for comment in comments]
        return result
    
    def _remove_empty_space(self, data:str) -> str:
        raw_data = re.split(r' ', data)
        if(len(raw_data)) == 0:
            return str()
        raw_data = list(map(lambda x: x.replace('\n', ''), raw_data))
        result = raw_data[0]
        if(len(raw_data)) == 1:
            return result
        for index_word in range(1, len(raw_data)):
            if raw_data[index_word]=='':
                continue
            result = result + ' ' + raw_data[index_word]
        return result

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