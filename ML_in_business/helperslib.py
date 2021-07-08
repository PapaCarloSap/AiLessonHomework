import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


def generate_dummies(df: pd.DataFrame, category_names: list) -> pd.DataFrame:
    result = df.copy()
    for category_name in category_names:
        result = pd.concat([result.drop(category_name, 1), pd.get_dummies(result[category_name], prefix=category_name)], 1)
    return result

def convert_category_text_to_number(df: pd.DataFrame, name:str) -> pd.Series:
    labelencoder = LabelEncoder()
    sr = df[name]
    labelencoder.fit(sr)
    nameclasses = labelencoder.classes_
    print('<< {} >>'.format(name))
    print('{:<5} {:<10}'.format('Index:', 'Value:'))
    for num_name in range(len(nameclasses)):
        print('{:<7} {:<10}'.format(num_name, nameclasses[num_name]))
    print('-'*10)
    return labelencoder.transform(sr)