# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython
from numpy.core.numerictypes import ScalarType

# %%
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from metrictool import MetricRegressionManager

import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

#%%
metric_manager = MetricRegressionManager()

# %% [markdown]
# ## Данные

# %%
df = pd.read_csv("Churn_Modelling.csv")
df.info()


# %%
df['Exited'].value_counts()


# %%
#разделим данные на train/test
X_train, X_test, y_train, y_test = train_test_split(df, df['Exited'], random_state=0)


# %%
#соберем наш простой pipeline, но нам понадобится написать класс для выбора нужного поля
class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X[self.column]
    
class NumberSelector(BaseEstimator, TransformerMixin):
    """
    Transformer to select a single column from the data frame to perform additional transformations on
    Use on numeric columns in the data
    """
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[[self.key]]
    
class OHEEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, key):
        self.key = key
        self.columns = []

    def fit(self, X, y=None):
        self.columns = [col for col in pd.get_dummies(X, prefix=self.key).columns]
        return self

    def transform(self, X):
        X = pd.get_dummies(X, prefix=self.key)
        test_columns = [col for col in X.columns]
        for col_ in self.columns:
            if col_ not in test_columns:
                X[col_] = 0
        return X[self.columns]


# %%
# Зададим списки признаков
categorical_columns = ['Geography', 'Gender', 'Tenure', 'HasCrCard', 'IsActiveMember']
continuous_columns = ['CreditScore', 'Age', 'Balance', 'NumOfProducts', 'EstimatedSalary']


# %%
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion


# %%
# Теперь нам нужно под каждый признак создать трансформер и объединить их в список
final_transformers = list()

for cat_col in categorical_columns:
    cat_transformer = Pipeline([
                ('selector', FeatureSelector(column=cat_col)),
                ('ohe', OHEEncoder(key=cat_col))
            ])
    final_transformers.append((cat_col, cat_transformer))
    
for cont_col in continuous_columns:
    cont_transformer = Pipeline([
                ('selector', NumberSelector(key=cont_col)), 
            ])
    final_transformers.append((cont_col, cont_transformer))


# %%
# Объединим все это в единый пайплайн
feats = FeatureUnion(final_transformers)
# пайплайн, который готовит признаки для моделирования.
feature_processing = Pipeline([('feats', feats)])

# %% [markdown]
# ## Модели
# %% [markdown]
# ### RandomForestClassifier

# %%
# Добавим модель
from sklearn.ensemble import RandomForestClassifier

model_name = 'RandomForestClassifier'

pipeline = Pipeline([
    ('features',feats),
    ('classifier', RandomForestClassifier(random_state = 42)),
])


# %%
# Обучим модель
pipeline.fit(X_train, y_train)


# %%
#наши прогнозы для тестовой выборки
preds = pipeline.predict_proba(X_test)[:, 1]
preds[:10]

# %% [markdown]
# Также нам нужно от вероятностей перейти к меткам классов. Для этого нужно подобрать порог, после которого мы считаем, что объект можно отнести к классу 1 (если вероятность больше порога - размечаем объект как класс 1, если нет - класс 0)

# %%
metric_manager.apply(model_name, y_test, preds)
metric = metric_manager.calc_metric(name=model_name)
metric.show_table()
metric_manager.show_confusion_matrix(model_name)

# %% [markdown]
# ### Бустинг

# %%
from catboost import CatBoostClassifier

model_name='CatBoostClassifier'
pipeline = Pipeline([
    ('features',feats),
    ('classifier', CatBoostClassifier(silent=True, random_state = 42)),
])

pipeline.fit(X_train, y_train)

preds = pipeline.predict_proba(X_test)[:, 1]

# %%
metric_manager.apply(model_name, y_test, preds)
metric = metric_manager.calc_metric(name=model_name)
metric.show_table()
metric_manager.show_confusion_matrix(model_name)

# %% [markdown]
# ### Логическая регрессия

# %%
from sklearn.preprocessing import StandardScaler

class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X[self.column]

class MyStandardScaler(BaseEstimator, TransformerMixin):
    __scaler = None

    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        if self.__scaler is None:
            self.__scaler = StandardScaler().fit(X[[self.column]])  
        return self

    def transform(self, X, y=None):
        return self.__scaler.transform(X[[self.column]])


# %%
# Теперь нам нужно под каждый признак создать трансформер и объединить их в список
final_transformers_v2 = list()

for cat_col in categorical_columns:
    cat_transformer = Pipeline([
                ('selector', FeatureSelector(column=cat_col)),
                ('ohe', OHEEncoder(key=cat_col))
            ])
    final_transformers_v2.append((cat_col, cat_transformer))
    
for cont_col in continuous_columns:
    cont_transformer = Pipeline([
                    ('selector', NumberSelector(key=cont_col))
                ,   ('scaler', MyStandardScaler(column=cont_col))
                #,   ('scaler', StandardScaler())
            ])
    final_transformers_v2.append((cont_col, cont_transformer))


# %%
X_train.describe()


# %%
# Объединим все это в единый пайплайн
feats_v2 = FeatureUnion(final_transformers_v2)
# пайплайн, который готовит признаки для моделирования.
feature_processing_v2 = Pipeline([('feats', feats_v2)])
fr = pd.DataFrame(feature_processing_v2.fit_transform(X_train))
fr.describe()

# %%
# ручное скалирование
scaler = StandardScaler().fit(X_train[continuous_columns])
df_test = X_train.copy()
df_test[continuous_columns] = scaler.transform(X_train[continuous_columns])
df_test.describe()
#pd.DataFrame(scaler.transform(X_train[continuous_columns])).describe()

# %%
from sklearn.linear_model           import LogisticRegression

model_name = 'LogisticRegression'
pipeline = Pipeline([
    ('features',feats_v2),
    ('classifier', LogisticRegression(random_state = 42)),
])
pipeline.fit(X_train, y_train)

#y_train_pred = pipeline.predict_proba(fr)[:, 1]
y_test_pred = pipeline.predict_proba(X_test)[:, 1]


# %%
metric_manager.apply(model_name, y_test, y_test_pred)
metric = metric_manager.calc_metric(name=model_name)
metric.show_table()
metric_manager.show_confusion_matrix(model_name)


# %%

metric_manager.calc_metrics()

# %%
