# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.series import Series
import seaborn as sns
from mlhelpertool import AttributeNamesManager

get_ipython().run_line_magic('matplotlib', 'inline')

# %% [markdown]
# ## Работа с данными
# %% [markdown]
# ## Описание переменных
# 
# ### данные банковского клиента
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | age | numeric | возраст |
# | job | categorical | текущая работа |
# | marital | categorical | семейное положение |
# | education | categorical | образование |
# | default | categorical | имеет ли кредит по умолчанию? |
# | housing | categorical | есть ли жилищный кредит? |
# | loan | categorical | есть ли личный кредит? |
# 
# ### связано с последним контактом текущей кампании 
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | contact | categorical | тип контактной связи |
# | month | categorical | последний месяц контакта в году |
# | day_of_week | categorical | последний контактный день недели |
# | duration | numeric | продолжительность последнего контакта, в секундах (числовое значение). Важное примечание: этот атрибут сильно влияет на целевой результат вывода (например, если длительность=0, то y="нет"). Тем не менее, продолжительность не известна до выполнения вызова. Кроме того, после окончания вызова y, очевидно, известен. Таким образом, эти входные данные следует включать только для целей сравнения и их следует отбросить, если предполагается создать реалистичную прогностическую модель. |
# 
# ### другие атрибуты
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | campaign | numeric | количество контактов, выполненных в ходе этой кампании и для данного клиента |
# | pdays | numeric | количество дней, прошедших после того, как с клиентом в последний раз связывались в рамках предыдущей кампании (числовое значение; 999 означает, что с клиентом ранее не связывались) |
# | previous | numeric | количество контактов, выполненных до этой кампании и для данного клиента |
# | poutcome | categorical | результат предыдущей маркетинговой кампании |
# 
# ### атрибуты социального и экономического контекста
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | emp.var.rate | numeric | коэффициент вариации занятости - квартальный показатель |
# | cons.price.idx | numeric | индекс потребительских цен - месячный показатель |
# | cons.conf.idx | numeric | индекс доверия потребителей - месячный показатель |
# | euribor3m | numeric | ставка euribor за 3 месяца - ежедневный показатель |
# | nr.employed | numeric | численность работников - квартальный показатель |
# 
# ### Выходная переменная (желаемая цель)
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | y | binary | зарегистрировал ли клиент срочный депозит? |

# %%
attribute_names = AttributeNamesManager(
    numeric = [
        'age', 
        'emp.var.rate',
        'cons.price.idx',
        'cons.conf.idx',
        'euribor3m',
        'nr.employed'
    ],
    category = [
        'job',
        'marital',
        'education',
        'default',
        'housing',
        'loan'
    ],
    target = 'y'
    )

# %%
df = pd.read_csv("bank-additional-full.csv", delimiter=';')
df.info()


# %%
df.head(10)


# %%
df[attribute_names.Target].value_counts()

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[attribute_names.Features], df[attribute_names.Target], random_state=0)

# %% [markdown]
# ## Преобразование данных к числам

#%%
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin

#%%
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

class NumberSelector(BaseEstimator, TransformerMixin):
    """
    Transformer to select a single column from the data frame to perform additional transformations on
    Use on numeric columns in the data
    """
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[[self.column]]

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

# строим пайплайн
test_transformers = list()

for cat_col in attribute_names.Categories:
    cat_transformer = Pipeline([
                ('selector', FeatureSelector(column=cat_col))
                #('selector', NumberSelector(column=cat_col))
                #, ('ohe', CategoryToNumberEncoder(column=cat_col))
            ])
    test_transformers.append((cat_col, cat_transformer))
    
# for cont_col in attribute_names.Numerics:
#     cont_transformer = Pipeline([
#                     ('selector', NumberSelector(key=cont_col))
#                 ,   ('scaler', MyStandardScaler(column=cont_col))
#                 #,   ('scaler', StandardScaler())
#             ])
#     final_transformers_v2.append((cont_col, cont_transformer))
    
# Объединим все это в единый пайплайн
feature_processing =Pipeline([
        ('features', FeatureUnion(test_transformers))
        ])

feature_processing.fit(X_train)
df = feature_processing.transform(X_train)
transform = feature_processing.transform(X_train)
test_df = pd.DataFrame(transform)
feature_processing.named_steps['features'].get_feature_names()
test_df.info()
test_df.describe()


# %% [markdown]
# ## Построение признаков

# %%
for name in attribute_names.Features:
  plt.subplot(1,2,1)
  sns.kdeplot(X_train[name])
  plt.subplot(1,2,2)
  plt.hist(X_train[name])
  plt.show()
