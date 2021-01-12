import Data_mining.hw2.project_1 as lib
import bs4
import codecs
import os


def test_get_old_price():
    #target = lib.Parser5ka('', None)
    product_path = get_file_path('product_1.xml')
    f=codecs.open(product_path, 'r')
    print (f.read())
    
    # bs4.BeautifulSoup(response.text, 'lxml')
    # target._get_old_price()

def get_file_path(file_path:str)->str:
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, file_path)