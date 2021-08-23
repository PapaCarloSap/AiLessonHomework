from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class RandomRecommendation:
    '''
    Random recommendation
    Случайные рекомендации
    не реализован
    '''
    __item_tag : str
    __items : pd.Series

    def __init__(self,
        /,
        item_tag : str
        ):
        self.__item_tag = item_tag

    def fit(self, df:pd.DataFrame):
        self.__items = df[self.__item_tag]

    def recommend(self, n:int=5)->List[np.array]:
        items = self.__items.array
        return np.random.choice(items, size=n, replace=False).tolist()

class PopularityRecommendation:
    '''
    Popularity-based recommendation
    не реализован
    '''
    # def popularity_recommendation(data, n=5):
    #     """Топ-n популярных товаров"""
        
    #     popular = data.groupby('item_id')['sales_value'].sum().reset_index()
    #     popular.sort_values('sales_value', ascending=False, inplace=True)
        
    #     recs = popular.head(n).item_id
        
    #     return recs.tolist()
    pass


class WeightRandomRecommendation:
    '''
    Weighted random recommender
    '''
    __item_tag : str
    __weight_tag : str
    __weight_name : str = 'weights'   
    __popularity : pd.DataFrame     # таблица items с приведенным к весу(__weight_name). Вес зависит от величины __weight_tag 


    def __init__(self,
        /,
        item_tag : str,
        weight_tag : str
        ):
        self.__item_tag = item_tag
        self.__weight_tag = weight_tag

    def fit(self, df:pd.DataFrame):
        self.__popularity = df.groupby(self.__item_tag)[self.__weight_tag].sum().reset_index()
        self.__popularity[self.__weight_name] = WeightRandomRecommendation.WeightCoverter(
            self.__popularity[self.__weight_tag]
            ).get_weights()

    def recommend(self, n:int=5)->List[np.array]:
        return np.random.choice(
            self.__popularity[self.__item_tag], 
            replace=False,
            p=self.__popularity[self.__weight_name], 
            size=n)

    class WeightCoverter():
        __data : pd.Series
        __sum_data : float

        def __init__(self, data:pd.Series)->None:
            self.__data = data
            self.__sum_data = data.sum()

        def get_weight(self, value: float)->float:
            return value/self.__sum_data

        def get_weights(self):
            return self.__data.apply(lambda x: self.get_weight(x))