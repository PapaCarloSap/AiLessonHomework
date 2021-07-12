

# def test_load_content_from_5ka():
#     target = hw1.Parser5ka()
#     assert target.load_products_by_category()

def test_get_url_category():
    import Data_mining.hw1.hw1 as hw1
    target = hw1.Parser5ka()
    assert target._get_url_category('111') == 'https://5ka.ru/api/v2/categories/111/'

def test_get_url_products_by_category():
    import Data_mining.hw1.hw1 as hw1
    target = hw1.Parser5ka()
    assert target._get_url_products_by_category('111') == 'https://5ka.ru/api/v2/special_offers/?store=&records_per_page=12&page=1&categories=111'