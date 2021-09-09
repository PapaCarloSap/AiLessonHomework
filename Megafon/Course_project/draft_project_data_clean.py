# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Курсовой проект

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import set_config
from Megafon.Course_project.data_manager import DataManager
import Megafon.Course_project.helper as helper
from Megafon.Course_project.metrictool import MetricRegressionManager


# %%
get_ipython().run_line_magic('matplotlib', 'inline')
set_config(display='diagram')
plt.style.use('ggplot')

# %% [markdown]
# ## Константы 

# %%
DATA_PATH = r'Megafon\Course_project\temp_data\data_train.csv'      # путь к связи пользователя и целевой переменной
FEATURES_PATH =r'Megafon\Course_project\temp_data\features.csv'     # путь к файлу с опиисанию пользователя
TARGET = 'target'                                                   # целевая переменная
USER_ID = 'id'                                                      # id ползователя
BUY_TIME = 'buy_time_convert'                                       # время регистрации данных
VAS_ID = 'vas_id'                                                   # подключаемая услуга
RANDOM_STATE = 1                                                    # привязка воспроизводимых случайных значениях
RELOAD_DATA_SOURCE = False                                          # True - Необходимо пересобрать обучающую выборуц из csv файлов 

#%%
# Глобальные переменные
metric_manager = MetricRegressionManager()

# %% [markdown]
# ## Обзор датасета 

# %%
data_manager=DataManager(DATA_PATH, FEATURES_PATH)
source_df:pd.DataFrame = None
source_df = data_manager.get_full_data(reload_csv = RELOAD_DATA_SOURCE, update_source = RELOAD_DATA_SOURCE)
source_df = source_df[:6000]                      #! для реальных расчетов убрать 
# if RELOAD_DATA_SOURCE:
#     source_df = data_manager.get_full_data(reload = True)
#     data_manager.save(source_df)
# else:
#     source_df = data_manager.get_full_data(reload = False)
# if True: # 
#     source_df, missing_df = data_manager.clean_data(source_df)
#     source_df = pd.concat([source_df, data_manager.get_nearest_data_by_date(missing_df)[0]])
#     data_manager.save(source_df) 
source_df.info()

# %%
source_df.dtypes

# %%
#source_df[VAS_ID] = source_df[VAS_ID].astype('int')
source_df[VAS_ID] = source_df[VAS_ID].astype('category')
source_df[TARGET] = source_df[TARGET].astype('int')
helper.show_distribution_variables_pie({'Распределение целевой переменной':source_df[TARGET], 'Распределение подкл. услуги':source_df[VAS_ID]})
source_df.reset_index()
source_df = pd.get_dummies(source_df)

# %%
helper.print_NaN_data(source_df)

# %%
# делим данные
from sklearn.model_selection import train_test_split
X_train:pd.DataFrame = None
X_test:pd.DataFrame = None
y_train:pd.DataFrame = None
y_test:pd.DataFrame = None
X_train, X_test, y_train, y_test = train_test_split(source_df.drop([TARGET, USER_ID, BUY_TIME], 1), source_df[TARGET], test_size=0.3,  random_state=RANDOM_STATE)
helper.show_distribution_variables_pie({'Train':y_train, 'Test':y_test})
# y_train.value_counts(normalize=True)
# y_test.value_counts(normalize=True)

# %%
# Пайплайн
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from Megafon.Course_project.helper_evaluating_model import show_roc_auc
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler

def model_research(name_estimator:str, estimator: Pipeline, df_x:pd.DataFrame, df_y:pd.Series):
    estimator.fit(df_x, df_y)
    y_pred = estimator.predict_proba(X_test)[:,1]
    metric_manager.apply(name_estimator, y_test, y_pred)

# #%%
# from imblearn.under_sampling import RandomUnderSampler
# target_counts = y_train.value_counts()[1]
# rus = RandomUnderSampler(sampling_strategy={0:target_counts*2, 1:target_counts}, random_state=RANDOM_STATE)
# #rus = RandomUnderSampler(sampling_strategy={0:200000, 1:42250}, random_state=RANDOM_STATE)
# X_resampled, y_resampled = rus.fit_sample(X_train, y_train)
# helper.show_distribution_variable_pie(y_resampled)

# %%
# Пайплайн для baseline
# Используем логистическую регрессию как наиболее быстродействующую

# %%
bl_model_name = 'Baseline'
bl_estimator = Pipeline([
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])

# значение метрики на кросс-валидации
#show_roc_auc(X_train, y_train, bl_estimator)

model_research(bl_model_name, bl_estimator, X_train, y_train)

# %%
bl_under_model_name = 'Baseline UnderSampler'
bl_under_estimator = Pipeline([
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])

target_counts = y_train.value_counts()[1]
rus = RandomUnderSampler(sampling_strategy={0:target_counts*2, 1:target_counts}, random_state=RANDOM_STATE)
#rus = RandomUnderSampler(sampling_strategy={0:200000, 1:42250}, random_state=RANDOM_STATE)
X_under_res, y_under_res = rus.fit_sample(X_train, y_train)
helper.show_distribution_variable_pie(y_under_res)

model_research(bl_under_model_name, bl_under_estimator, X_under_res, y_under_res)

# # %%
# bl_over_model_name = 'Baseline OverSampler'
# bl_over_estimator = Pipeline([
#     ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
# ])
# target_counts = y_train.value_counts()[1]
# #rus = RandomUnderSampler(sampling_strategy={0:5000, 1:20000}, random_state=RANDOM_STATE)
# rus = RandomUnderSampler(sampling_strategy=0.95, random_state=RANDOM_STATE)
# #rus = RandomUnderSampler(sampling_strategy={0:200000, 1:42250}, random_state=RANDOM_STATE)
# X_over_res, y_over_res = rus.fit_sample(X_train, y_train)
# helper.show_distribution_variable_pie(y_over_res)

# model_research(bl_over_model_name, bl_over_estimator, X_over_res, y_over_res)

# %%
bl_over_model_name = 'Baseline OverSampler'

preprocessor = ColumnTransformer(
    transformers=[
        (COMMENT_VECTORIZER, text_transformer, COMMENT)
        # думаю здесь добавить дополнительные признаки как длинну коментария и т.д.
        ]
    , remainder='drop'
    )

bl_over_estimator = Pipeline([
    ('preprocessor', RandomUnderSampler(0.95)),
    ('undersampler', preprocessor),
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])
target_counts = y_train.value_counts()[1]
#rus = RandomUnderSampler(sampling_strategy={0:5000, 1:20000}, random_state=RANDOM_STATE)
rus = RandomUnderSampler(sampling_strategy=0.95, random_state=RANDOM_STATE)
#rus = RandomUnderSampler(sampling_strategy={0:200000, 1:42250}, random_state=RANDOM_STATE)
X_over_res, y_over_res = rus.fit_sample(X_train, y_train)
helper.show_distribution_variable_pie(y_over_res)

model_research(bl_over_model_name, bl_over_estimator, X_over_res, y_over_res)

# -------------------------------------------------------------------------------------------------------------
#%%
metric_manager.show_full_report(
    name_negative = 'Не подключил услугу',
    name_positive = 'Подключение услуги'
)

metric_manager.show_united_auc()

# %%


# %%