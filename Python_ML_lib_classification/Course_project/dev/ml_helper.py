import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import r2_score


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

# def change_str(df: pd.DataFrame):
#     for cat_colname in df.select_dtypes(include='object').columns[1:]:
#         df = pd.concat([df, pd.get_dummies(df[cat_colname], prefix=cat_colname)], axis=1)

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