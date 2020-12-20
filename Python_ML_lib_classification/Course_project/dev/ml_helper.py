import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import r2_score
from sklearn.metrics import classification_report, f1_score, precision_score, recall_score


#pd.options.display.float_format = '{:,.2f}'.format

def get_object_value_counts(df: pd.DataFrame):
    """Вывести value_counts() для всех Pandas.Series 

    Args:
        df (pd.DataFrame): Pandas.DataFrame
    """
    for cat_colname in df.select_dtypes(include='object').columns:
        print(str(cat_colname) + '\n\n' + str(df[cat_colname].value_counts()) + '\n' + '*' * 100 + '\n')

def get_nan_count(df: pd.DataFrame):
    print(len(df) - df.count())

def get_nan_percent(df: pd.DataFrame):
    print((len(df) - df.count())/len(df)*100)

def fillna_float64_median(df: pd.DataFrame):
    for cat_colname in df.select_dtypes(include='float64').columns[0:]:
        df[cat_colname].fillna(df[cat_colname].median(), inplace=True)

def fillna_dummines_mode(df: pd.DataFrame):
    for cat_colname in df.select_dtypes(include='object').columns[0:]:
        df[cat_colname].fillna(df[cat_colname].mode()[0], inplace=True)

def get_classification_report(y_train_true, y_train_pred, y_test_true, y_test_pred):
    """Отчет по результату класификации

    Args:
        y_train_true ([type]): [description]
        y_train_pred ([type]): [description]
        y_test_true ([type]): [description]
        y_test_pred ([type]): [description]
    """
    print('TRAIN\n\n' + classification_report(y_train_true, y_train_pred))
    print('TEST\n\n' + classification_report(y_test_true, y_test_pred))
    print('CONFUSION MATRIX\n')
    print(pd.crosstab(y_test_true, y_test_pred))

def balance_df_by_target(df: pd.DataFrame, target_name: str) -> pd.DataFrame:
    """Oversampling

    Args:
        df ([type]): pd.DataFrame
        target_name ([type]): имя целевой переменной

    Returns:
        [type]: [description]
    """
    target_counts = df[target_name].value_counts()
    major_class_name = target_counts.argmax()
    minor_class_name = target_counts.argmin()
    disbalance_coeff = int(target_counts[major_class_name] / target_counts[minor_class_name]) - 1
    for i in range(disbalance_coeff):
        sample = df[df[target_name] == minor_class_name].sample(target_counts[minor_class_name])
        df = df.append(sample, ignore_index=True)
    return df.sample(frac=1)

def fillna_dummines_mode_ex(df: pd.DataFrame):
    for cat_colname in df.select_dtypes(include='object'):
        for colname in df[cat_colname].keys():
            if pd.isna(df[cat_colname][colname]):
                df[cat_colname][colname] = df[cat_colname].mode()

def add_id(df: pd.DataFrame):
    df['Id'] = df.index.tolist()

def main():
    print('HelloWorld')

if __name__ == '__main__':
    main()