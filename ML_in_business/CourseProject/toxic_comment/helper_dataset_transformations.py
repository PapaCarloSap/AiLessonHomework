import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
import re
from enum import Enum
from deprecated import deprecated
from razdel import tokenize
import pymorphy2
import nltk
import nltk.corpus as nltk_cor
import tqdm

nltk.download('stopwords')

class Language(Enum):
    En = 1
    Ru = 2


class tempEstimator(BaseEstimator,TransformerMixin):
    def __init__(self,string):
        self.string = string

    def fit(self,X):
        return self

    def transform(self,X):
        return X.take([0], axis=1).to_numpy()
        #return np.full(X.shape, self.string).reshape(-1,1)

    def get_feature_names(self):
        return self.string

class TextCleanerTransform(BaseEstimator,TransformerMixin):
    def __init__(self, language:Language):
        self.language = language

    def fit(self,X, y=None):
        return self

    def transform(self,X):
        '''
        очистка текста
        на выходе очищеный текст
        '''
        if type(X) is pd.Series:
            clean_texts = list()
            for text in tqdm.tqdm(X.values.tolist()):
                clean_texts.append(self.__clean_text(text))
            return np.array(clean_texts)
            #result = pd.DataFrame({X.name: clean_texts}, dtype="string")
            #result[X.name] = np.array(list(map(lambda text: self.__clean_text(text) , X.values)))
            #result = X.values.apply(lambda text: self.__clean_text(text))
        elif type(X) is pd.DataFrame:
            clean_texts = list()
            for text in tqdm.tqdm(X.iloc[:, 0].values.tolist()):
                clean_texts.append(self.__clean_text(text))
            return np.array(clean_texts)
        else:
            raise Exception('для type(X) отсутствует обработчик')
            #result = X.apply(lambda col: col.apply(lambda text: self.__clean_text(text)))
        
        return result

    def get_feature_names(self):
        return ['clean']

    def __clean_text(self, text)->str:
        if not isinstance(text, str):
            text = str(text)
    
        text = text.lower()
        text = re.sub('[\s]', ' ', text)
        if self.language == Language.En:
            text = re.sub('[^A-z\s]', ' ', text)
        elif self.language == Language.Ru:
            text = re.sub('[^А-я\s]', ' ', text)
        else:
            text = re.sub('[^A-z\s]', ' ', text)
        # Python 3.10
        # match self.language:
        #     case Language.En:
        #         text = re.sub('[^A-z]', '', text)
        #     case Language.Ru:
        #         text = re.sub('[^А-я]', '', text)
        #     case _:
        #         text = re.sub('[^A-z]', '', text)
        return text

    @deprecated(reason='оставил для примера, может что то от сюда можно забрать еще')
    def __old_clean_text(self, text):
        #return 'ok'
        if not isinstance(text, str):
            text = str(text)
    
        text = text.lower()
        text = text.strip('\n').strip('\r').strip('\t')
        text = re.sub("-\s\r\n\|-\s\r\n|\r\n", '', str(text))

        text = re.sub("[0-9]|[-—.,:;_%©«»?*!@#№$^•·&()]|[+=]|[[]|[]]|[/]|", '', text)
        text = re.sub(r"\r\n\t|\n|\\s|\r\t|\\n", ' ', text)
        text = re.sub(r'[\xad]|[\s+]', ' ', text.strip())
    
        #tokens = list(tokenize(text))
        #words = [_.text for _ in tokens]
        #words = [w for w in words if w not in stopword_ru]
        
        #return " ".join(words)
        return text

class TextLemmatizationTransform(BaseEstimator,TransformerMixin):
    def __init__(self, language:Language):
        self.__language = language
        self.__cache = {}
        self.__morph = pymorphy2.MorphAnalyzer()
        self.__generate_stopwords_ru()

    def fit(self,X, y=None):
        return self

    def transform(self,X:np.array):
        '''
        лемматизация текста
        '''
        clean_texts = list()
        #for text in tqdm.tqdm(list(X.iloc[:, 0].values)):
        for text in tqdm.tqdm(X.tolist()):
            clean_texts.append(self.__lemitization(text))
        #result[X.iloc[:, 0].name] = np.array(clean_texts)
        return np.array(clean_texts)
        # result = X.apply(lambda col: col.apply(lambda text: self.__lemitization(text)))
        # return result


    def get_feature_names(self):
        return ['lemmatization']

    def __generate_stopwords_ru(self):
        with open('ML_in_business/CourseProject/toxic_comment/stopwords.txt') as f:
            additional_stopwords = [w.strip() for w in f.readlines() if w]
        self.__stopwords_ru = set(nltk_cor.stopwords.words('russian') + additional_stopwords)

    '''
    text = "она ее ей ней неё ней"
    result = ['она', 'ее', 'ей', 'ней', 'неё', 'ней']
    '''
    def __generate_tokens(self, text:str)->list:
        tokens = list(tokenize(text))
        return [_.text for _ in tokens]

    '''
    tokens = ['она', 'ее', 'ей', 'ней', 'неё', 'ней']
    result = ['она', 'она', 'она', 'она', 'она', 'она']
    '''
    def __normalize_tokens(self, tokens):
        return [self.__morph.parse(tok)[0].normal_form for tok in tokens]

    def __remove_stopwords(self, tokens, min_length=1):
        if not self.__stopwords_ru:
            return tokens
        stopwords = self.__stopwords_ru
        tokens = [tok
                for tok in tokens
                if tok not in stopwords and len(tok) >= min_length]
        return tokens

    
    def __lemitization(self, text:str):
        tokens = self.__generate_tokens(text)
        normalize_tokens = self.__normalize_tokens(tokens)
        words = self.__remove_stopwords(normalize_tokens, min_length=1)
        return ' '.join(words)

class tempTransform(BaseEstimator,TransformerMixin):
    
    def fit(self,X):
        return self

    def transform(self,X):
        return X.iloc[:, 0]
        #return np.full(X.shape, self.string).reshape(-1,1)

    def get_feature_names(self):
        return 'test'