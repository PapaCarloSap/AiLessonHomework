import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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