import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class Undersampler(BaseEstimator,TransformerMixin):
    def fit(self,X):
        return self

    def transform(self,X):
        return X
        #return np.full(X.shape, self.string).reshape(-1,1)
