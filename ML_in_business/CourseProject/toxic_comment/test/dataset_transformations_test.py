import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from ML_in_business.CourseProject.toxic_comment.dataset_transformations_helper import Language, TextCleanerTransform, tempEstimator
import collections 


# def test_TextCleanerTransform():
#     # docs=["the house had a tiny little mouse", 
#     #     "the cat saw the mouse", 
#     #     "the mouse ran away from the house", 
#     #     "the cat finally ate the mouse", 
#     #     "the end of the mouse story"
#     #     ]

#     df = pd.DataFrame({ 'text': ["the house had a tiny little mouse \n", 
#                                 "the cat saw the mouse!!!!", 
#                                 "the mouse ran-away... from the\t house", 
#                                 "the cat finally?, ate the mouse", 
#                                 "the end of the mouse story"
#                                 ],
#                         'target': [0,1,0,1,0]
#         })

#     preprocessor = ColumnTransformer(
#         transformers=[
#             ('text', TextCleanerTransform(), ['text'])
#             #('temp', tempEstimator('AAA'), ['text'])
#             ]
#             , remainder='passthrough'
#             )
#             #('text_clean', tempEstimator('AAA'), ['text'])])

#     clean_text = Pipeline(
#         steps=[
#             ('preprocessor', preprocessor)
#             ])
#     pr = preprocessor.fit_transform(df)
#     clean_text.fit(df)
#     assert False

def test_TextCleanerTransform_v2():
    from ML_in_business.CourseProject.toxic_comment.dataset_transformations_helper import Language, TextCleanerTransform

    expected = ["the house had a tiny little mouse", 
        "the cat saw the mouse", 
        "the mouse ranaway from the house", 
        "the cat finally ate the mouse", 
        "the end of the mouse story"
        ]
    df = pd.DataFrame({ 'text': ["the house had a tiny little mouse \n", 
                                "the cat saw the mouse!!!!", 
                                "the mouse ran-away... from the\thouse", 
                                "the cat finally?, ate the mouse", 
                                "the end of the mouse story"
                                ],
                        'target': [0,1,0,1,0]
        })

    # act
    text_tranformer = Pipeline(steps=[
        ('clean', TextCleanerTransform(Language.En))
        ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('text', text_tranformer, 'text')
            ]
        , remainder='drop'
    )

    result = preprocessor.fit(df)

    # assert
    assert collections.Counter(expected) == collections.Counter(result.tolist())
    
    # col = result.iloc[:, 0].astype(str).str
    # for num in range(len(text_expected)):
    #     assert col.contains(text_expected[num])[num], 'Не совподают строки позции \'{0}\' \nExpected: \t {1} \nResult: \t {2}'.format(
    #         num,
    #         text_expected[num],
    #         result.iloc[:, 0][num]
    #     )

def test_Lemmatization():
    from ML_in_business.CourseProject.toxic_comment.dataset_transformations_helper import Language, TextLemmatizationTransform

    expected = [
        'дом жить маленький мышь', 
        'кошка увидеть мышь', 
        'мышь убежать дом', 
        'кошка съесть мышь', 
        'конец история мыший'
        ]
    # df = pd.DataFrame({ 
    #     'text': [
    #         "в доме живет маленькая мышь", 
    #         "кошка увидела мышь", 
    #         "мышь убежала из дома", 
    #         "кошка наконец съела мышь", 
    #         "конец истории с мышью"
    #         ]
    #     })
    data = np.array([
            "в доме живет маленькая мышь", 
            "кошка увидела мышь", 
            "мышь убежала из дома", 
            "кошка наконец съела мышь", 
            "конец истории с мышью"
            ])

    # act
    text_tranformer = Pipeline(steps=[
        ('lemmatization', TextLemmatizationTransform(Language.Ru))
        ])

    result = text_tranformer.fit_transform(data)

    # assert
    assert collections.Counter(expected) == collections.Counter(result.tolist())

    # проверка для  DataFrame
    # for num in range(len(expected)):
    #     assert result.iloc[:, 0][num]==expected[num], 'Не совподают строки позции \'{0}\' \nExpected: \t {1} \nResult: \t {2}'.format(
    #         num,
    #         expected[num],
    #         result.iloc[:, 0][num]
    #     )

def test_generate_tokens():
    from ML_in_business.CourseProject.toxic_comment.dataset_transformations_helper import Language, TextLemmatizationTransform
    lem = TextLemmatizationTransform(Language.Ru)
    expected = ['она', 'ее', 'ей', 'ней', 'неё', 'ней']
    text = "она ее ей ней неё ней"
    tokens = lem._TextLemmatizationTransform__generate_tokens(text)
    assert collections.Counter(expected) == collections.Counter(tokens)

def test_normalize_tokens():
    from ML_in_business.CourseProject.toxic_comment.dataset_transformations_helper import Language, TextLemmatizationTransform
    lem = TextLemmatizationTransform(Language.Ru)
    expected = ['она', 'она', 'она', 'она', 'она', 'она']
    text = ['она', 'ее', 'ей', 'ней', 'неё', 'ней']
    tokens = lem._TextLemmatizationTransform__normalize_tokens(text)
    assert collections.Counter(expected) == collections.Counter(tokens)

def test_TfidfVectorizer():
    from sklearn.feature_extraction.text import TfidfVectorizer
    data = [
        'дом жить маленький мышь', 
        'кошка увидеть мышь', 
        'мышь убежать дом', 
        'кошка съесть мышь', 
        'конец история мыший'
        ]

    df = pd.DataFrame({ 
        'text': [
            "в доме живет маленькая мышь", 
            "кошка увидела мышь", 
            "мышь убежала из дома", 
            "кошка наконец съела мышь", 
            "конец истории с мышью"
            ]
        })

    tf0 = TfidfVectorizer()
    tf0.fit(data)
    X_train_tfidf = tf0.transform(df)
    X_train_tfidf.shape
    assert X_train_tfidf.shape[0]==1
    assert X_train_tfidf.shape[1]==11
    # отсортируем по силе
    pd.DataFrame(tf0.idf_, index=tf0.get_feature_names(),columns=["idf_weights"]).sort_values(by=['idf_weights'])

def test_Pipeline():
    from ML_in_business.CourseProject.toxic_comment.dataset_transformations_helper import Language, TextLemmatizationTransform, tempTransform
    from sklearn.feature_extraction.text import TfidfVectorizer

    expected = [
        'дом жить маленький мышь', 
        'кошка увидеть мышь', 
        'мышь убежать дом', 
        'кошка съесть мышь', 
        'конец история мыший'
        ]
    df = pd.DataFrame({ 
        'text': [
            "в доме живет маленькая мышь", 
            "кошка увидела мышь", 
            "мышь убежала из дома", 
            "кошка наконец съела мышь", 
            "конец истории с мышью"
            ]
        })

    # act
    text_tranformer = Pipeline(steps=[
        ('clean', TextCleanerTransform(Language.Ru))
        , ('lem', TextLemmatizationTransform(Language.Ru))
        , ('tf0', TfidfVectorizer())
        ])

    result = text_tranformer.fit_transform(df)
    assert result.shape[0]==5
    assert result.shape[1]==11
    pd.DataFrame(text_tranformer.named_steps['tf0'].idf_, index=text_tranformer.named_steps['tf0'].get_feature_names(),columns=["idf_weights"]).sort_values(by=['idf_weights'])

