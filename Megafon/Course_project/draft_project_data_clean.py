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

# Управление моделями
# Baseline
BL_MODEL_NAME = 'Baseline'   
RUN_BASELINE = True
# Кросс-валидация на бейзлайне
RUN_CROSS_VALID = False  
# 
BL_UNDER_LOGREG_NAME = 'LogReg feat_proc us'        
RUN_UNDER_LOGREG = True
#
BL_OVER_MODEL_NAME = 'LogReg feat_proc os'
RUN_OVER_LOGREG = True
#
GBC_NAME = 'GradientBoostingClassifier'
RUN_GBC = True
#
RFC_NAME = 'RandomForestClassifier'
RUN_RFC= True


#%%
# Глобальные переменные
metric_manager = MetricRegressionManager()

# %% [markdown]
# ## Обзор датасета 

# %%
data_manager=DataManager(DATA_PATH, FEATURES_PATH)
source_df:pd.DataFrame = None
source_df = data_manager.get_full_data(reload_csv = RELOAD_DATA_SOURCE, update_source = RELOAD_DATA_SOURCE)
#source_df = source_df[:6000]                      #! для реальных расчетов убрать 
source_df.info()

# %%
source_df.dtypes

# %%
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
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
from Megafon.Course_project.transformers import ColumnSelector

set_config(display='diagram')

# %%
def model_research(name_estimator:str, estimator: Pipeline, df_x:pd.DataFrame, df_y:pd.Series):
    estimator.fit(df_x, df_y)
    y_pred = estimator.predict_proba(X_test)[:,1]
    metric_manager.apply(name_estimator, y_test, y_pred)

#%% Sampler
def get_undersampler():
    target_counts = y_train.value_counts()[1]
    rus :RandomUnderSampler = RandomUnderSampler(sampling_strategy={0:target_counts*2, 1:target_counts}, random_state=RANDOM_STATE)
    return rus.fit_sample(X_train, y_train)

def get_oversampler():
    ros = RandomOverSampler(sampling_strategy=0.95, random_state=RANDOM_STATE)
    return ros.fit_sample(X_train, y_train)



# %% BASELINE
bl_estimator = Pipeline([
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])
if RUN_BASELINE: model_research(BL_MODEL_NAME, bl_estimator, X_train, y_train)

# значение метрики на кросс-валидации
if RUN_CROSS_VALID: show_roc_auc(X_train, y_train, bl_estimator)

# -------------------------------------------------------------------------------------------------------------
# %%
preprocessor = make_pipeline(
    ColumnSelector(columns=list(sorted_features.categorical | sorted_features.numeric)),
    FeatureUnion(transformer_list=[
        ("numeric_features", make_pipeline(
            ColumnSelector(list(sorted_features.numeric)),
            #SimpleImputer(strategy="mean"),
            StandardScaler()
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

# -------------------------------------------------------------------------------------------------------------
# %%
bl_over_estimator = Pipeline([
    ('preprocessor', preprocessor),
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])
if RUN_OVER_LOGREG:
    X_res, y_res =get_oversampler()
    model_research(BL_OVER_MODEL_NAME, bl_over_estimator, X_res, y_res)

# -------------------------------------------------------------------------------------------------------------
# %%
bl_under_estimator = Pipeline([
    ('preprocessor', preprocessor),
    ('log_reg', LogisticRegression(random_state=RANDOM_STATE, n_jobs=-1))
])
if RUN_UNDER_LOGREG:
    X_res, y_res =get_undersampler()
    model_research(BL_UNDER_LOGREG_NAME, bl_under_estimator, X_res, y_res)

# %% Поиск параметров
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform
from sklearn.metrics import f1_score, make_scorer
# подбор параметров 
hyperparameters = dict(log_reg__C=uniform(loc=0, scale=4), log_reg__penalty=['l2', 'l1'])
clf = RandomizedSearchCV(bl_under_estimator, hyperparameters, random_state=RANDOM_STATE, n_iter=50, cv=5, verbose=0, n_jobs=-1, scoring=make_scorer(f1_score, average='macro'))
X_res, y_res =get_undersampler()
search = clf.fit(X_res, y_res)
print(search.best_params_)
# {'log_reg__C': 2.1326611398920683, 'log_reg__penalty': 'l2'}

# %% Отбор признаков в пайплайнах
from sklearn.feature_selection import SelectFromModel

fs_pipe = make_pipeline(
    preprocessor,
    SelectFromModel(LogisticRegression(penalty='l2', C=2.133, random_state=RANDOM_STATE), threshold=1e-5),
)
preprocessor.fit(X_train)
fs_pipe.fit(X_train, y_train)
num_insignificant_features = preprocessor.transform(X_test).shape[1] - fs_pipe.transform(X_test).shape[1]
print('Логистическая регрессия из SelectFromModel обнулила около {insign:.3f}% признаков.'.format(insign=num_insignificant_features/preprocessor.transform(X_test).shape[1] * 100))

# %%
logreg_configured_estimator = Pipeline([
    ('preprocessor', preprocessor),
    ('log_reg', LogisticRegression(penalty='l2', C=1.253, random_state=RANDOM_STATE, n_jobs=-1))
])
if RUN_UNDER_LOGREG:
    X_res, y_res =get_undersampler()
    model_research(BL_UNDER_LOGREG_NAME, bl_under_estimator, X_res, y_res)

# -------------------------------------------------------------------------------------------------------------
# %%
if RUN_GBC:
    gbc_estimator = Pipeline([
        ('preprocessor', preprocessor),
        ('gbc', GradientBoostingClassifier(random_state=RANDOM_STATE))
    ])

    hyperparameters = dict(
        gbc__max_depth=[3,6,10],
        gbc__n_estimators=[100,500,1000, 1200, 1500],
        gbc__min_samples_split=[2,5,8,11],
        gbc__learning_rate=[0.01,0.05,0.1,0.5,1.0],
        gbc__max_features=['sqrt', 'log2']
        )
    clf = RandomizedSearchCV(
        gbc_estimator, 
        hyperparameters, 
        n_iter = 100, 
        cv = 5, 
        random_state=RANDOM_STATE, 
        verbose=0, n_jobs=-1, scoring=make_scorer(f1_score, average='macro'))
    X_res, y_res =get_undersampler()
    search = clf.fit(X_res, y_res)
    print(search.best_params_)
# {'gbc__n_estimators': 1500, 'gbc__min_samples_split': 5, 'gbc__max_features': 'sqrt', 'gbc__max_depth': 3, 'gbc__learning_rate': 0.01}

#%%
if RUN_GBC:
    gbc_estimator = Pipeline([
        ('preprocessor', preprocessor),
        ('gbc', GradientBoostingClassifier(
            n_estimators = 1500,
            min_samples_split = 5,
            max_features= 'sqrt',
            max_depth = 3,
            learning_rate = 0.01,
            random_state=RANDOM_STATE))
    ])
    X_res, y_res =get_undersampler()
    model_research(GBC_NAME, gbc_estimator, X_res, y_res)

# -------------------------------------------------------------------------------------------------------------
# %%
if RUN_RFC:
    rfg_estimator = Pipeline([
        ('preprocessor', preprocessor),
        ('rfc', RandomForestClassifier(random_state=RANDOM_STATE, n_jobs=-1))
    ])

    hyperparameters = dict(
        rfc__n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1000, num = 10)],
                        rfc__max_features = ['log2', 'sqrt'],
                        rfc__max_depth = [int(x) for x in np.linspace(start = 1, stop = 15, num = 15)],
                        rfc__min_samples_split = [int(x) for x in np.linspace(start = 2, stop = 50, num = 10)],
                        rfc__min_samples_leaf = [int(x) for x in np.linspace(start = 2, stop = 50, num = 10)],
                        rfc__bootstrap = [True, False]
                        )
    clf = RandomizedSearchCV(rfg_estimator, 
                            hyperparameters, 
                            n_iter = 100, 
                            cv = 5, 
                            random_state=RANDOM_STATE, 
                            verbose=0, n_jobs=-1, scoring=make_scorer(f1_score, average='macro'))
    X_res, y_res =get_undersampler()
    search = clf.fit(X_res, y_res)
    print(search.best_params_)
    # {'rfc__n_estimators': 900, 'rfc__min_samples_split': 28, 'rfc__min_samples_leaf': 2, 'rfc__max_features': 'sqrt', 'rfc__max_depth': 14, 'rfc__bootstrap': False}

# %%
if RUN_RFC:
    rfg_estimator = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestClassifier(
            n_estimators = 900,
            min_samples_split = 28,
            min_samples_leaf = 2,
            max_features = 'sqrt',
            max_depth = 14,
            bootstrap = False,
            random_state=RANDOM_STATE, n_jobs=-1))
    ])
    X_res, y_res =get_undersampler()
    model_research(RFC_NAME, rfg_estimator, X_res, y_res)

# -------------------------------------------------------------------------------------------------------------
#%% Metrics
metric_manager.show_full_report(
    name_negative = 'Не подключил услугу',
    name_positive = 'Подключение услуги',
    spec_thr=0.5
)

metric_manager.show_full_report(
    name_negative = 'Не подключил услугу',
    name_positive = 'Подключение услуги'
)

metric_manager.show_united_auc()

# -------------------------------------------------------------------------------------------------------------


#%%
hyperparameters = dict(log_reg__C=uniform(loc=0, scale=4), log_reg__penalty=['l2', 'l1'])
clf = RandomizedSearchCV(bl_over_estimator, hyperparameters, random_state=RANDOM_STATE, n_iter=50, cv=5, verbose=0, n_jobs=-1, scoring=make_scorer(f1_score, average='macro'))
X_res, y_res =get_undersampler()
#preprocessor.fit(X_res)
search = clf.fit(X_res, y_res)
search.best_params_
# {'log_reg__C': 1.2530940677291005, 'log_reg__penalty': 'l2'}
# -------------------------------------------------------------------------------------------------------------




#%% Metrics
metric_manager.show_full_report(
    name_negative = 'Не подключил услугу',
    name_positive = 'Подключение услуги',
    spec_thr=0.5
)

metric_manager.show_united_auc()

# %%


# %%