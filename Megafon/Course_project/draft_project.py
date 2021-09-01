# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Курсовой проект

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import set_config
from Megafon.Course_project.data_manager import DataManager


# %%
get_ipython().run_line_magic('matplotlib', 'inline')
set_config(display='diagram')

# %% [markdown]
# ## Константы 
DATA_PATH = r'Megafon\Course_project\temp_data\data_train.csv'
FEATURES_PATH =r'Megafon\Course_project\temp_data\features.csv'
TARGET = 'target'

# %% [markdown]
# ## Обзор датасета 

# %%
data_manager=DataManager(DATA_PATH, FEATURES_PATH)
source_df:pd.DataFrame = data_manager.get_full_data(reload = False)
source_df.info()

# %%
#source_df[TARGET].value_counts(normalize=True)
