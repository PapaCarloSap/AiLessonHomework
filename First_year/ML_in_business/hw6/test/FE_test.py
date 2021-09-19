import unittest
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

def test_category_pipeline():
    import ML_in_business.hw6.TransformerLib as target
    df = pd.DataFrame({ 'brand': ['aaaa', 'asdfasdf', 'sadfds', 'NaN'],
                        'category': ['asdf', 'asfa', 'asdfas', 'as'],
                        'num1': [1, 1, 0, 0],
                        'target': [0.2, 0.11, 1.34, 1.123]})

    numeric_features = ['num1']
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    categorical_features = ['brand', 'category']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    clf = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor',  LinearRegression())])
    clf.fit(df.drop('target', 1), df['target'])
    result = clf.named_steps['preprocessor'].transformers_[1][1].named_steps['onehot'].get_feature_names(categorical_features)

    assert result.sort()==['brand_NaN' 'brand_aaaa' 'brand_asdfasdf' 'brand_sadfds' 'category_as' 'category_asdf' 'category_asdfas' 'category_asfa'].sort()

def test_ColumnTransformer():
    import pandas as pd
    from sklearn.compose import ColumnTransformer
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.preprocessing import OneHotEncoder
    from ML_in_business.hw6.TransformerLib import MyTempEncoder, tempEstimator
    from sklearn import set_config

    X = pd.DataFrame(
        {'city': ['London', 'London', 'Paris', 'Sallisaw'],
        'title': ["His Last Bow", "How Watson Learned the Trick", "A Moveable Feast", "The Grapes of Wrath"],
        'expert_rating': [5, 3, 4, 5],
        'user_rating': [4, 5, 4, 3]})

    # column_trans = ColumnTransformer(
    #     [('city_category', OneHotEncoder(dtype='int'),['city']),
    #     ('title_bow', CountVectorizer(), 'title')],
    #     remainder='drop')
    
    # column_trans= Pipeline([
    #             ('selector', MyTempEncoder())
    #         ])

    column_trans = ColumnTransformer(
        [   
            #('city_category', OneHotEncoder(dtype='int'),['city']),
            ('myEncoder', tempEstimator('AAAA'), ['title'])],
        remainder='passthrough'
        #remainder='drop'
    )
    
    #HTML representation of Pipeline
    #set_config(display='diagram')
    set_config(display='text')
    column_trans

    column_trans.fit_transform(X)
    names = column_trans.get_feature_names()
    arr = column_trans.transform(X)
    assert True