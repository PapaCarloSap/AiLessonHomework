# from io import TextIOWrapper
import os
import pandas as pd
from pathlib import Path
import datetime
from typing import Tuple

# class HeaderName():
#     def __init__(self, data_names:List[str], features_name:List[str]):
#         self.__data_names:List[str] = data_names
#         self.__feature_names:List[str] = features_name

#     @property
#     def data_names(self)->List[str]:
#         return self.__data_names 

#     @property
#     def feature_names(self)->List[str]:
#         return self.__feature_names

#     @property
#     def all_names(self)->List[str]:
#         return self.__data_names + self.__feature_names

class DataManager(): 
    #__line_header_count:int = 1
    __name_source_df_pickle = 'temp_source_df.pkl'
    __name_data_df_pickle = 'temp_data_df.pkl'
    __name_features_df_pickle = 'temp_features_df.pkl'

    def __init__(self, path_data, path_features):
        self.__path_data:Path = Path(path_data)
        self.__path_features:Path = Path(path_features)

    # def get_short_data(self, percent:float=0.3)->pd.DataFrame:
    #     header_names = HeaderName(self.__get_data_names(), self.__get_feature_names())
    #     result:pd.DataFrame = pd.DataFrame(columns=header_names.all_names)
    #     with self.__path_data.open() as data_file:
    #         count_line = (self.__get_count_line(file=data_file)-self.__line_header_count) * percent
    #         data_file.seek(0)
    #         data_file.readline()
    #         num_line = 0
    #         with self.__path_features.open() as features_file:
    #             for line_data in data_file:
    #                 num_line+=1
    #                 if num_line > count_line:
    #                     break
    #                 record:pd.Series = pd.Series(line_data.rstrip().split(',')[1:], index=header_names.data_names)
    #                 features = self.__get_features_by_user_id(user_id = record[0], file = features_file)
    #                 if(features is None):
    #                     print(f'for user_id = \'{record[0]}\' not found features')
    #                     continue
    #                 record = pd.concat([record, pd.Series(features[3:], index=header_names.feature_names)])
    #                 result = result.append(record, ignore_index=True)
    #     return result

    # def __get_data_names(self):
    #     with self.__path_data.open() as data_file:
    #         return data_file.readline().rstrip().split(',')[1:]

    # def __get_feature_names(self):
    #     with self.__path_features.open() as features_file:
    #         return features_file.readline().rstrip().split('\t')[3:]

    # def __get_features_by_user_id(self, user_id:str, file:TextIOWrapper)->list:
    #     file.seek(0)
    #     file.readline()
    #     for line_file in file:
    #         features = line_file.rstrip().split('\t')
    #         if features[1] == user_id:
    #             return features
    #     return None

    # def __get_count_line(self, file:TextIOWrapper)->int:
    #     file.seek(0)
    #     return sum(1 for line in file)

    def get_full_data(self, reload_csv:bool = False, update_source:bool= False)-> pd.DataFrame:
        data_df : pd.DataFrame = None
        features_df : pd.DataFrame = None
        if reload_csv or (not os.path.exists(self.__name_data_df_pickle) or not os.path.exists(self.__name_features_df_pickle)):
            data_df, features_df = self._init_data_and_features()
        else:
            data_df = pd.read_pickle(self.__name_data_df_pickle)
            features_df = pd.read_pickle(self.__name_features_df_pickle)

        if update_source or not os.path.exists(self.__name_features_df_pickle):
            source_df = self._generate_source_data(data_df, features_df)
            source_df, missing_features_for_user = self._clean_data(source_df)
            nearest_df = self._get_forward_data_by_date(missing_features_for_user, data_df, features_df)
            nearest_df, missing_features_for_user = self._clean_data(nearest_df)
            source_df = pd.concat([source_df, nearest_df])
            self.save_data(source_df)
            return source_df
        else:
            return self.load_data()

    def _init_data_and_features(self)-> Tuple[pd.DataFrame]:
        """Загрузить данные из csv файла

        Returns:
            Tuple[pd.DataFrame]: (пользователь-услуга, описание пользователя)
        """
        data_df = pd.read_csv(str(self.__path_data), sep=',').drop(columns=['Unnamed: 0'])
        data_df['buy_time_convert'] = data_df['buy_time'].transform(datetime.datetime.fromtimestamp)
        data_df = data_df.drop(columns='buy_time')
        data_df.to_pickle(self.__name_data_df_pickle)

        features_df = pd.read_csv(str(self.__path_features), sep='\t').drop(columns=['Unnamed: 0'])
        features_df['buy_time_convert'] = features_df['buy_time'].transform(datetime.datetime.fromtimestamp)
        features_df = features_df.drop(columns='buy_time')
        features_df.to_pickle(self.__name_features_df_pickle)

        return data_df, features_df
            

    def _generate_source_data(self
        , data_df:pd.DataFrame = None
        , features_df:pd.DataFrame = None
    )->pd.DataFrame:
        """Выбираем последние данные до указанной даты

        Args:
            data_df ([type]): [description]
            features_df ([type]): [description]

        Returns:
            [type]: [description]
        """
        if data_df is None:
            data_df = pd.read_pickle(self.__name_data_df_pickle)
        if features_df is None:
            features_df = pd.read_pickle(self.__name_features_df_pickle)
        data_df = data_df.sort_values(by=['buy_time_convert'])
        features_df = features_df.sort_values(by=['buy_time_convert'])
        source_df = pd.merge_asof(data_df, features_df, on='buy_time_convert', by='id')
        return source_df

    def _clean_data(self, df:pd.DataFrame)-> Tuple[pd.DataFrame]:
        """Удалить строки где отсутствуют описание для пользователей 

        Args:
            df (pd.DataFrame): данные с пользователями

        Returns:
            Tuple[pd.DataFrame]: (очищенные данные, удаленные данные)
        """
        missing_features = df[df.isnull().sum(axis=1)>252]
        if missing_features.shape[0]>0:
            print(f'Features missing for {missing_features.shape[0]} users.')
        return df.drop(missing_features.index), missing_features

    def _get_forward_data_by_date(self
        , df:pd.DataFrame
        , data_df:pd.DataFrame = None
        , features_df:pd.DataFrame = None
    )->Tuple[pd.DataFrame]:
        """Выбираем ближайшее по дате описание пользователя и объеденяем с подключаемой услугой

        Args:
            df (pd.DataFrame): [description]

        Returns:
            Tuple[pd.DataFrame]: [description]
        """
        if data_df is None:
            data_df = pd.read_pickle(self.__name_data_df_pickle)
        if features_df is None:
            features_df = pd.read_pickle(self.__name_features_df_pickle)
        data_df = df[['id', 'buy_time_convert']].join(data_df.set_index(['id', 'buy_time_convert']), on=['id', 'buy_time_convert']).sort_values(by=['buy_time_convert'])
        features_df = features_df.sort_values(by=['buy_time_convert'])
        #source_df = pd.merge_asof(df[['id', 'vas_id', 'target', 'buy_time_convert']], features_df, on='buy_time_convert', by='id', direction='forward')
        source_df = pd.merge_asof(
            data_df, 
            features_df, 
            on='buy_time_convert', 
            by='id', 
            direction='forward')
        return source_df

    def save_data(self, source_df:pd.DataFrame, suffix:str=''):
        source_df.to_pickle(self.__name_source_df_pickle+suffix)

    def load_data(self, suffix:str='')->pd.DataFrame:
        return pd.read_pickle(self.__name_source_df_pickle)

    def get_data_for_users(self, path_to_users:str)-> Tuple[pd.DataFrame]:
        data_df = pd.read_csv(str(Path(path_to_users)), sep=',').drop(columns=['Unnamed: 0'])
        data_df['buy_time_convert'] = data_df['buy_time'].transform(datetime.datetime.fromtimestamp)
        data_df = data_df.drop(columns='buy_time')
        features_df = pd.read_pickle(self.__name_features_df_pickle)
        features_df = features_df.drop(columns='buy_time')
        user_features_df = self._generate_source_data(data_df, features_df)
        return self._clean_data(user_features_df)

    