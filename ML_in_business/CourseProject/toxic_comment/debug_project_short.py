# %%
from IPython import get_ipython

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ML_in_business.CourseProject.toxic_comment.metrictool import MetricRegressionManager


# %%
get_ipython().run_line_magic('matplotlib', 'inline')

# %%
# константы
TARGET = 'toxic'
COMMENT = 'comment'
COMMENT_VECTORIZER = 'comment_vectorizer'

# %%
# глобальные переменные
# Пусть:
#       штраф за пропущенный корректный коммент 100 р
#       штраф за пропущенный токсичный коммент в 10 р
metric_manager = MetricRegressionManager(
    fine_good=100,  # штраф за пропущенный корректный коммент
    fine_toxic=10,  # штраф за пропущенный токсичный коммент
    )

# %%
df = pd.read_csv("ML_in_business/CourseProject/toxic_comment/labeled.csv")
# df = pd.DataFrame({ COMMENT: ["the house had a tiny little mouse \n", 
#                             "the cat saw the mouse!!!!", 
#                             "the mouse ran-away... from the\thouse", 
#                             "the cat finally?, ate the mouse", 
#                             "the end of the mouse story"
#                             ],
#                     TARGET: [0,1,0,1,0]
#     })
df.info()
#df = df[:6000]        #! для реальных расчетов убрать 

#%%
df[TARGET] = df[TARGET].astype('bool')
df[TARGET].value_counts(normalize=True)

# %%
# делим данные
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop(TARGET, 1), df[TARGET], test_size=0.3,  random_state=1)
y_train.value_counts(normalize=True)
y_test.value_counts(normalize=True)

# %%
from sklearn import set_config
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from ML_in_business.CourseProject.toxic_comment.helper_dataset_transformations import TextCleanerTransform, Language, TextLemmatizationTransform
from sklearn.naive_bayes import MultinomialNB

set_config(display='diagram')

# Pipeline
from sklearn.linear_model import LogisticRegression

model_name = 'LogisticRegression'
text_transformer = Pipeline(steps=[
            ('clean', TextCleanerTransform(language = Language.Ru))
        ,   ('lemmatization', TextLemmatizationTransform(Language.Ru))
        ,   ('vectorizer', TfidfVectorizer(
                    # sublinear_tf=True,      # Примените сублинейное масштабирование tf, т. е. замените tf на 1 + log(tf).
                    # strip_accents='unicode',
                    # analyzer='word',            
                    # token_pattern=r'\w{1,}',# разделитель токена
                    # #stop_words='english',
                    # ngram_range=(1, 1),     # каждое слово отдельно
                    # max_features=1000       # размер словаря
        ))
        ])

preprocessor = ColumnTransformer(
    transformers=[
        (COMMENT_VECTORIZER, text_transformer, COMMENT)
        # думаю здесь добавить дополнительные признаки как длинну коментария и т.д.
        ]
    , remainder='drop'
    )

pipe_clf = Pipeline(steps=[
        ('preprocessor', preprocessor)
    ,   ('regressor',  LogisticRegression(C=0.1, solver='sag'))
    #,   ('regressor',  MultinomialNB())
    ])

# %%
# from sklearn.model_selection import cross_val_score
# проверим как модель поведет себя на  на неизвестных ей данных
# cv_scores = cross_val_score(clf, X_train, y_train, cv=3, scoring='roc_auc')
# print('\n--')
# print('Перекростно-проверочная точность: %.3f +/- %.3f' % (np.mean(cv_scores), np.std(cv_scores)))
from ML_in_business.CourseProject.toxic_comment.helper_evaluating_model import show_roc_auc
show_roc_auc(X_train, y_train, pipe_clf)


#%%
# обучение пайплайна
pipe_clf.fit(X=X_train, y=y_train)
preds = pipe_clf.predict_proba(X_test)[:, 1]
metric_manager.apply(model_name, y_test, preds)
preds[:10]

# %%
# Посмотрим на графики метрик чтобы выбрать порог
metric_manager.get_experiment(model_name).show_proba_calibration_plots(
    name_positive = 'Обычные',
    name_negative = 'Токсичные'
)

# %%
# Судя по графику Probability histogram вероятность определения токсичнычх коментариев смещена в лево из-за чего чаще возникают ошибки на определения токсичных коментариев.
# Для решения надо попробовать добавить больше признаков для их определения. Возможно это длинна строки, отношение количество знаков препинания к длинне строки, отношение количества ошибок к длинне строки и т.д. 
# Попробовать сбалансировать таргет признак (Undersampling)

# %%
# Определим порог срабатывания по f1 score
metric = metric_manager.calc_metric(name=model_name)
metric.show_table()
metric.Confusion_matrix.show_picture(
    title = 'Матрица ошибок',
    name_positive = 'Обычные',
    name_negative = 'Токсичные'
    )
metric.Confusion_matrix.show_metric()

# %%
#  FPR = 0.11 -> 11% всех комментариев будут помечены как токсичные некорректно
#  TNR = 0.89 -> модель может автоматически фильтровать 89% токсичных комментариев

# %%
# Экономическая часть
threshold, profit = metric_manager.get_experiment(model_name).show_profit_calibration_plots()
print(
    'При пороге: {0:.3f} Минимальный расход будет состовлять: {1} руб.'
    .format(
        threshold,
        profit
    )
)

# %%
# Приведем метрику к порогу 0.394
profit_threshold = threshold
metric = metric_manager.get_experiment(model_name).calc_metric(specified_thr=profit_threshold)
metric.Confusion_matrix.show_picture(
    title = 'Матрица ошибок',
    name_positive = 'Обычные',
    name_negative = 'Токсичные'
    )
metric.Confusion_matrix.show_metric()

# Если максимизировать по затратам то ввидно, что модель стала очень боятся штраф за пропуск токсичных коментарии и готово банить обычные коментарии
# Если максимизировать по f1 score то модель становится более сбалансированой, но несет дополнительные экономические издержки

# %%