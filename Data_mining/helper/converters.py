import datetime
import re


class StatusCodeError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_date_dd_mon_year(content:str)->datetime:
        raw_data = re.split(r' ', content)
        return datetime.datetime(
            int(raw_data[2]), 
            _monthToNum(raw_data[1]),
            int(raw_data[0])
            )

def _monthToNum(shortMonth):
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