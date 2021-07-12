from urllib.parse import unquote, quote


def test_parse_to_dict():
    import Data_mining.helper.conv_url as prs
    data='["~#iM", ["isSiteUserLoading", true, "interior3D", ["^0", ["id", "145", "name", "Tofas", "transliteration", "tofas"]]]]'
    url_data = quote(data)
    converter = prs.DecodeURIComponent(url_data)
    result = converter.to_dict()
    assert len(result)==1

def test_parse_array_to_dict():
    import Data_mining.helper.conv_url as prs
    data='[["id", "79", "name", "Isdera", "transliteration", "isdera"], ["id", "145", "name", "Tofas", "transliteration", "tofas"]]'
    url_data = quote(data)
    converter = prs.DecodeURIComponent(url_data)
    result = converter.to_dict()
    assert len(result)==2
