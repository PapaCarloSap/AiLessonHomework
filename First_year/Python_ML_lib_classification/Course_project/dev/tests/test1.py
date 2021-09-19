import numpy as np
from numpy.core.numeric import NaN
import pandas as pd
import os

import sys
sys.path.append('/Python_ML_lib_classification/Course_project/dev/')

TRAIN_DATASET_PATH = 'course_project_train.csv'
TEST_DATASET_PATH = 'course_project_test.csv'
TARGET = 'Credit Default'

print(os.getcwd())
df_train = pd.read_csv('./Python_ML_lib_classification/Course_project/dev/' + TRAIN_DATASET_PATH)
df_test = pd.read_csv('./Python_ML_lib_classification/Course_project/dev/' + TEST_DATASET_PATH)

def main():
    for colname in df_train['Years in current job'].keys():
        if pd.isna(df_train['Years in current job'][colname]):
            df_train['Years in current job'][colname] = df_train['Years in current job'].mode()

if __name__ == "__main__":
  main()