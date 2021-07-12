import bs4
import codecs
import os
import datetime


# def test_get_post_contetn_1():
#     #target = lib.Parser5ka('', None)
#     product_path = get_file_path('post_with_comment.html')
#     f=codecs.open(product_path, 'r')
#     content = bs4.BeautifulSoup(f.read(), 'lxml')
#     parser = lib.GbParse()
#     data = parser._post_parse(parser.home_url, content)
#     assert len(data['comments']) == 3

def test_get_post_contetn_2():
    import Data_mining.hw3.gb_blog_parse as lib
    import Data_mining.hw3.database as db_lib
    #target = lib.Parser5ka('', None)
    product_path = get_file_path('post_no_comment.html')
    f=codecs.open(product_path, 'r')
    content = bs4.BeautifulSoup(f.read(), 'lxml')
    parser = lib.GbParse()
    data = parser._post_parse(parser.home_url, content)
    assert len(data['comments']) == 0
    
def test_write_to_db():
    import Data_mining.hw3.gb_blog_parse as lib
    import Data_mining.hw3.database as db_lib
    db = db_lib.Database(os.environ['SQLITE_DBURL_TEST'])
    db.create_post(
        {
            'post_data': {
                'url': 'https://geekbrains.ru/', 
                'title': 'Открываем факультет Cloud Data Engineer в GeekBrains', 
                'post_image': 'https://d2xzmw6cctk25h.cloudfront.net/geekbrains/public/ckeditor_assets/pictures/10412/retina-1ce53076475b52da5f7c76f0e4b77eb2.png', 
                'date': datetime.datetime(2020, 12, 28, 0, 0), 
                'num_watch': 1364
            }, 
            'author': {
                'url': 'https://geekbrains.ru/users/63', 
                'name': 'Geek Brains'
            }, 
            'tags': [
                {
                    'name': 'программирование', 
                    'url': 'https://geekbrains.ru/posts?tag=программирование'
                }, 
                {
                    'name': 'cloud-data-engineering', 
                    'url': 'https://geekbrains.ru/posts?tag=cloud-data-engineering'
                }], 
            'comments': [
                {
                    'data_comment_id': 698836, 
                    'author': {'url': 'https://geekbrains.ru/users/2142884', 'name': 'Степан Федосеев'},
                    'content': 'Зачем отдельный факультет, если можно расширить факультет Data Engineer?'
                }, 
                {
                    'data_comment_id': 697925, 
                    'author': {'url': 'https://geekbrains.ru/users/253104', 'name': 'Артем Груздов'},
                    'content': 'А полную стоимость курса принцпиально нигде не пишите, чтобы не пугать?'
                }, 
                {
                    'data_comment_id': 697609, 
                    'author': {'url': 'https://geekbrains.ru/users/929441', 'name': 'Виталий Шишков'},
                    'content': 'Давненько ждал подобного факультета на Geekbrains, дождался и поступил!!! Ждем начала обучения:-)'
                }]
            }
    )
    assert True

def test_remove_empty_space():
    parser = lib.GbParse()
    result = parser._remove_empty_space('Geek\n                                            Brains')
    assert result == 'Geek Brains'

def get_file_path(file_path:str)->str:
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, file_path)