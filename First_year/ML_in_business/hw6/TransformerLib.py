import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder


class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X[self.column]
        
    def get_feature_names(self):
        return [self.__column]

class CategoryToNumberEncoder(BaseEstimator, TransformerMixin):
    
    def __init__(self, column:str):
        self.__encoder = LabelEncoder()
        self.__column = column

    def fit(self, X:pd.Series, y=None):
        if(self.__column != X.name):
            return self
        self.__encoder.fit(X)  
        nameclasses = self.__encoder.classes_
        print('<< {} >>'.format(X.name))
        print('{:<5} {:<10}'.format('Index:', 'Value:'))
        for num_name in range(len(nameclasses)):
            print('{:<7} {:<10}'.format(num_name, nameclasses[num_name]))
        print('-'*10)
        return self

    def transform(self, X, y=None):
        if(self.__column != X.name):
            return X
        unique_values = X.unique()
        for item in unique_values:
            if item not in self.__encoder.classes_:
                raise ValueError("Выборка имеет значение \'{0}\', которое отсутствует в тренеровочной коллекции".format(item))
        a = self.__encoder.transform(X)
        return a

    def get_feature_names(self):
        return [self.__column]

class MyTempEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X

class tempEstimator(BaseEstimator,TransformerMixin):
    def __init__(self,string):
        self.string = string

    def fit(self,X):
        return self

    def transform(self,X):
        return X.take([0], axis=1).to_numpy()
        #return np.full(X.shape, self.string).reshape(-1,1)

    def get_feature_names(self):
        return self.string