import pandas as pd
import numpy as np
from typing import Dict
import matplotlib.pyplot as plt


def print_NaN_data(df:pd.DataFrame):
    """Вывести процент признаков имеющие null-значение

    Args:
        df (pd.DataFrame): [description]
    """
    num_null = (df.isnull().sum() > 0).sum()
    if num_null == 0:
        print("Null-значение отсутствуют")
    else:
        print("Имеются Null-значение в размере %.3f%% от выборки" % float(num_null/df.shape[1]*100))

def show_distribution_variable_bar(df:pd.DataFrame):    
    """Показать распределение переменной (bar)

    Args:
        df (pd.DataFrame): [description]
    """
    (df.value_counts()/df.shape[0]).plot(kind='bar', title='Распределение переменной');
    print(df.value_counts(normalize=True))

def show_distribution_variable_pie(df:pd.DataFrame):
    """Показать распределение переменной (circle)

    Args:
        df (pd.DataFrame): [description]
    """
    ax = df.value_counts().plot.pie(autopct="%.2f")
    _ = ax.set_title("Распределение")

def show_distribution_variables_pie(data:Dict[str, pd.DataFrame]):
    num = len(data)
    fig, axs = plt.subplots(ncols=num, figsize=(8, 4))
    for i, (name, df) in enumerate(data.items()):
        axs[i] = df.value_counts().plot.pie(autopct="%.2f", ax=axs[i])
        _ = axs[i].set_title(name)
    fig.tight_layout()