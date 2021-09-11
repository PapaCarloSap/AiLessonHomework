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
from Megafon.Course_project.analyzertool import FeatureAnalyzer


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
source_df.info()

# %%
source_df.dtypes

# %%
#source_df[VAS_ID] = source_df[VAS_ID].astype('int')
#source_df[VAS_ID] = source_df[VAS_ID].astype('category')
source_df[TARGET] = source_df[TARGET].astype('int')
helper.show_distribution_variables_pie({'Распределение целевой переменной':source_df[TARGET], 'Распределение подкл. услуги':source_df[VAS_ID]})
source_df.reset_index()

# %%
helper.print_NaN_data(source_df)

#%%
# Определение типа признаков
feature_analyzer:FeatureAnalyzer = FeatureAnalyzer(features = source_df.drop([TARGET, USER_ID, BUY_TIME], 1), target=source_df[TARGET])
feature_analyzer.show_feature_unique()
sorted_features = feature_analyzer.share_featres_by_types()
# X_nunique = source_df.drop([TARGET, USER_ID, BUY_TIME], 1).apply(lambda x: x.nunique(dropna=False))
# plt.title("Распределение уникальных значений признаков")
# X_nunique.hist(bins=100, figsize=(10, 5))
# f_all = set(X_nunique.index.tolist())

# %%
# делим данные
from sklearn.model_selection import train_test_split
X_train:pd.DataFrame = None
X_test:pd.DataFrame = None
y_train:pd.DataFrame = None
y_test:pd.DataFrame = None
X_train, X_test, y_train, y_test = train_test_split(source_df.drop([TARGET, USER_ID, BUY_TIME], 1), source_df[TARGET], test_size=0.3,  random_state=RANDOM_STATE)
helper.show_distribution_variables_pie({'Train':y_train, 'Test':y_test})

# %%
# Пайплайн
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn import set_config
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from Megafon.Course_project.helper_evaluating_model import show_roc_auc
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
from Megafon.Course_project.transformers import ColumnSelector

set_config(display='diagram')

# %%
def model_research(name_estimator:str, estimator: Pipeline, df_x:pd.DataFrame, df_y:pd.Series):
    estimator.fit(df_x, df_y)
    y_pred = estimator.predict_proba(X_test)[:,1]
    metric_manager.apply(name_estimator, y_test, y_pred)



# %%
bl_model_name = 'Baseline'
bl_estimator = Pipeline([
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])

# значение метрики на кросс-валидации
#show_roc_auc(X_train, y_train, bl_estimator)

model_research(bl_model_name, bl_estimator, X_train, y_train)

#%% Sampler
def get_undersampler():
    target_counts = y_train.value_counts()[1]
    rus :RandomUnderSampler = RandomUnderSampler(sampling_strategy={0:target_counts*2, 1:target_counts}, random_state=RANDOM_STATE)
    return rus.fit_sample(X_train, y_train)

def get_oversampler():
    ros = RandomOverSampler(sampling_strategy=0.95, random_state=RANDOM_STATE)
    return ros.fit_sample(X_train, y_train)

# %%
bl_over_model_name = 'LogisticRegression with feature processing'
preprocessor = make_pipeline(
    ColumnSelector(columns=list(sorted_features.categorical | sorted_features.numeric)),
    FeatureUnion(transformer_list=[
        ("numeric_features", make_pipeline(
            ColumnSelector(list(sorted_features.numeric)),
            #SimpleImputer(strategy="mean"),
            #StandardScaler()
        )),
        ("categorical_features", make_pipeline(
            ColumnSelector(list(sorted_features.categorical)),
            #SimpleImputer(strategy="most_frequent"),
            OneHotEncoder(handle_unknown='ignore')
        ))
        # ("boolean_features", make_pipeline(
        #     ColumnSelector(f_binary),
        # ))
    ])
)

# X_res, y_res =get_undersampler()
# a= preprocessor.fit_transform(X_res, y_res)
# print(a)

##%%
bl_over_estimator = Pipeline([
    ('preprocessor', preprocessor),
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])
X_res, y_res =get_undersampler()
model_research(bl_over_model_name, bl_over_estimator, X_res, y_res)

# -------------------------------------------------------------------------------------------------------------
#%%
metric_manager.show_full_report(
    name_negative = 'Не подключил услугу',
    name_positive = 'Подключение услуги'
)

metric_manager.show_united_auc()

# %%


# %%