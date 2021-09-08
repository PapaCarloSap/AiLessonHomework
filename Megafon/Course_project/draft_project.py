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
RELOAD_DATA_SOURCE = True                                          # True - Необходимо пересобрать обучающую выборуц из csv файлов 

#%%
# Глобальные переменные
metric_manager = MetricRegressionManager()

# %% [markdown]
# ## Обзор датасета 

# %%
data_manager=DataManager(DATA_PATH, FEATURES_PATH)
source_df:pd.DataFrame = None
source_df = data_manager.get_full_data(reload_csv = RELOAD_DATA_SOURCE, update_source = RELOAD_DATA_SOURCE)
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
#source_df[VAS_ID] = source_df[VAS_ID].astype('category')
source_df[TARGET] = source_df[TARGET].astype('int')
helper.show_distribution_variables_pie({'Распределение целевой переменной':source_df[TARGET], 'Распределение подкл. услуги':source_df[VAS_ID]})
source_df.reset_index()
#source_df = pd.get_dummies(source_df)

# %%
helper.print_NaN_data(source_df)

# %%
# делим данные
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(source_df.drop([TARGET, USER_ID, BUY_TIME, VAS_ID], 1), source_df[TARGET], test_size=0.3,  random_state=RANDOM_STATE)
helper.show_distribution_variables_pie({'Train':y_train, 'Test':y_test})
# y_train.value_counts(normalize=True)
# y_test.value_counts(normalize=True)

# %%
# Пайплайн
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from Megafon.Course_project.helper_evaluating_model import show_roc_auc

# %%
# Пайплайн для baseline
# Используем логистическую регрессию как наиболее быстродействующую
from sklearn.linear_model import LogisticRegression
model_name = 'Baseline'

# %%
bl_estimator = Pipeline([
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])

#%%
from imblearn.under_sampling import RandomUnderSampler
#rus = RandomUnderSampler(sampling_strategy={0:50000, 1:26050}, random_state=RANDOM_STATE)
rus = RandomUnderSampler(sampling_strategy={0:200000, 1:42250}, random_state=RANDOM_STATE)
X_resampled, y_resampled = rus.fit_sample(X_train, y_train)
helper.show_distribution_variable_pie(y_resampled)

# %%
#bl_estimator.fit(X_train, y_train)
bl_estimator.fit(X_resampled, y_resampled)
# model_lr = LogisticRegression()
# model_lr.fit(X_train, y_train)
# pred = model_lr.predict_proba(X_test)[:,1]
pred = bl_estimator.predict_proba(X_test)[:,1]
metric_manager.apply(model_name, y_test, pred)

#%%
plt.title("Baseline: распределение предсказаний модели")
plt.hist(pred[~y_test.astype(bool)], bins=100, color='r', alpha=0.7)
plt.hist(pred[y_test.astype(bool)], bins=100, color='b', alpha=0.7)

# %%
# Выбор порога
metric_manager.get_experiment(model_name).show_proba_calibration_plots(
    name_positive = 'Подключение услуги',
    name_negative = 'Не подключил услугу'
)

# %%
show_roc_auc(X_train, y_train, bl_estimator)
# %%
