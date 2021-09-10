import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Set 


class SortedFeatres:
    __all:Set[str] = None
    __const:Set[str] = None
    __numeric:Set[str] = None
    __binary:Set[str] = None
    __categorical:Set[str] = None

    def __init__(self, 
        all:Set[str], 
        const:Set[str], 
        numeric:Set[str], 
        binary:Set[str], 
        categorical:Set[str]
    ):
        self.__all = all
        self.__const = const
        self.__numeric = numeric
        self.__binary = binary
        self.__categorical = categorical

    @property
    def all(self)->Set[str]:
        """Все признаки"""
        return self.__all

    @property
    def const(self)->Set[str]:
        """Константные признаки"""
        return self.__const

    @property
    def numeric(self)->Set[str]:
        """Вещественные признаки"""
        return self.__numeric

    @property
    def binary(self)->Set[str]:
        """Бинарные признаки"""
        return self.__binary

    @property
    def categorical(self)->Set[str]:
        """Категориальные признаки"""
        return self.__categorical
    

class FeatureAnalyzer:
    __features: pd.DataFrame = None
    __target: pd.Series = None
    __feature_unique : pd.Series = None

    def __init__(self, features:pd.DataFrame, target:pd.Series):
        self.__features = features
        self.__target = target
        self.__feature_unique = features.apply(lambda x: x.nunique(dropna=False))

    def share_featres_by_types(self) ->SortedFeatres:
        all = self.get_all()
        const = self.get_const()
        numeric= self.get_numeric()
        f_other=all - (numeric | const)
        binary = self.get_binary(f_other=f_other)
        f_other= f_other - binary
        categorical = self.get_categorical(f_other=f_other)
        if self.__feature_unique.shape[0] == len(const) + len(binary) + len(numeric) + len(categorical):
            return 
        return SortedFeatres(
            all= self.get_all(),
            const = self.get_const(), 
            numeric = numeric, 
            binary = binary,
            categorical = categorical
        )
        
    def get_all(self)->Set[str]:
        return set(self.__feature_unique.index.tolist())

    def get_const(self)->Set[str]:
        return set(self.__feature_unique[self.__feature_unique == 1].index.tolist())

    def get_numeric(self)->Set[str]:
        f_numeric = (self.__features.fillna(0).astype(int).sum() - self.__features.fillna(0).sum()).abs()
        return set(f_numeric[f_numeric > 0].index.tolist())

    def get_binary(self, f_other) ->Set[str]:
        return set(self.__features.loc[:, f_other].columns[(
                      (self.__features.loc[:, f_other].max() == 1) & \
                      (self.__features.loc[:, f_other].min() == 0) & \
                      (self.__features.loc[:, f_other].isnull().sum() == 0))])

    def get_categorical(self, f_other:Set[str]) ->Set[str]:
        return set(self.__feature_unique.loc[f_other][self.__feature_unique.loc[f_other] <= 10].index.tolist())

    def show_feature_unique(self):
        """Распределение уникальных значений признаков"""
        plt.title("Распределение уникальных значений признаков")
        self.__feature_unique.hist(bins=100, figsize=(10, 5))