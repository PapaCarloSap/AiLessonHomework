import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler


class UnderSamplerTransformer(BaseEstimator, TransformerMixin):
    _sampler : RandomUnderSampler = None
    _x_train:pd.DataFrame = None
    _y_train:pd.DataFrame = None

    def __init__(self, sampling_strategy, random_state):
        self._sampler = RandomUnderSampler(sampling_strategy=sampling_strategy, random_state=random_state)

    def fit(self,X, y=None):
        self._x_train = X
        self._y_train = y
        return self

    def transform(self, X):
        if X is self._x_train:
            X_res, y_res = self._sampler.fit_sample(self._x_train, self._y_train)
            return X_res, y_res
        return X

class OverSamplerTransformer(RandomOverSampler,TransformerMixin):
    def transform(self, X, y=None):
        return X
