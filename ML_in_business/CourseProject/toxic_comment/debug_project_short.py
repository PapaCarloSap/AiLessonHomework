# %%
from IPython import get_ipython

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# %%
get_ipython().run_line_magic('matplotlib', 'inline')

# %%
TARGET = 'toxic'
COMMENT = 'comment'
COMMENT_VECTORIZER = 'comment_vectorizer'

# %%
df = pd.read_csv("ML_in_business/CourseProject/toxic_comment/labeled.csv")
df.info()

#%%
df[TARGET] = df[TARGET].astype('bool')
df[COMMENT] = df[COMMENT].astype('str')
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
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from ML_in_business.CourseProject.toxic_comment.dataset_transformations_helper import TextCleanerTransform, Language, TextLemmatizationTransform, tempTransform
from sklearn.naive_bayes import MultinomialNB

set_config(display='diagram')
# Pipeline
text_transformer = Pipeline(steps=[
            ('clean', TextCleanerTransform(language = Language.Ru))
        ,   ('lemmatization', TextLemmatizationTransform(Language.Ru))
        ,   ('vectorizer', TfidfVectorizer(
                    sublinear_tf=True,      # Примените сублинейное масштабирование tf, т. е. замените tf на 1 + log(tf).
                    strip_accents='unicode',
                    analyzer='word',            
                    token_pattern=r'\w{1,}',# разделитель токена
                    #stop_words='english',
                    ngram_range=(1, 1),     # каждое слово отдельно
                    max_features=1000       # размер словаря
        ))
        ])

preprocessor = ColumnTransformer(
    transformers=[
        (COMMENT_VECTORIZER, text_transformer, COMMENT)
        # думаю здесь добавить дополнительные признаки как длинну коментария и т.д.
        ]
    , remainder='drop'
    )

clf = Pipeline(steps=[
        ('preprocessor', preprocessor)
    ,   ('regressor',  LogisticRegression(C=0.1, solver='sag'))
    #,   ('regressor',  MultinomialNB())
    ])
clf

# %%
from sklearn.model_selection import cross_val_score
# кросс-валидацию
cv_scores = cross_val_score(clf, X_train, y_train, cv=3, scoring='roc_auc')
cv_score = np.mean(cv_scores)
print('CV score is {}'.format(cv_score))

#%%
# обучение пайплайна
clf.fit(X=X_train, y=y_train)
preds = clf.predict_proba(X_test)[:, 1]
preds[:10]

# %%
# Метрики
# TODO: Возможно надо попробовать добавить расчет метрик в Pipeline но не факт что получится. Хоят в конструктор добавить  y_test 
# TODO: а в predict_proba(X_test) и после этого вывести метрику
