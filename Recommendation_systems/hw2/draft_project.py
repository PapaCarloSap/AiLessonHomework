# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import zipfile

with zipfile.ZipFile('Recommendation_systems/hw2/data.zip', 'r') as zip_ref:
    zip_ref.extractall('Recommendation_systems/hw2/temp_data')


# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Для работы с матрицами
from scipy.sparse import csr_matrix, coo_matrix

# Детерминированные алгоритмы
from implicit.nearest_neighbours import ItemItemRecommender, CosineRecommender, TFIDFRecommender, BM25Recommender

# Метрики
from implicit.evaluation import train_test_split
from implicit.evaluation import precision_at_k, mean_average_precision_at_k, AUC_at_k, ndcg_at_k


# %%
data = pd.read_csv('Recommendation_systems/hw2/temp_data/data/retail_train.csv')
data.head(2)


# %%
test_size_weeks = 3

data_train = data[data['week_no'] < data['week_no'].max() - test_size_weeks]
data_test = data[data['week_no'] >= data['week_no'].max() - test_size_weeks]

# %% [markdown]
# 
# 
# %% [markdown]
# ### Задание 0. Товар 999999
# 
# #### На вебинаре мы использовали товар 999999 - что это за товар?  
# > Это пустой товар который необходим чтобы ввести пользователя(произвести холодный старт). 
# #### Зачем он нужен?  
# > Необходим чтобы пометить что пользователь не проивзаимодействовал ни с одним товаром
# #### Используя этот товар мы смещаем качество рекомендаций. В какую сторону?   
# > Думаю что смещение идет в худшую сторону. Почему не знаю, но кажется что этот товар может иметь влияние на сегметирование пользователей и мешать подбору подходящего пользователя
# *Можно ли удалить этот товар?
# > Думаю да, когда пользователь провзаимодействует с настоящим товаром. Удалить товар и переобучить модель    
# #### Уберите этот товар (**внимание**: это можно сделать разными способами!) и сравните с качеством на семинаре.
# 
# >т.к. в коде выше он не задан то как вариант убрать 999999
# ```python
# # добавил
# data_train.loc[~data_train['item_id'].isin(top_5000), 'item_id'] = 999999
# # удалил
# data_train.loc[data_train['item_id']==999999] = 0
# ```
# %% [markdown]
# - Не вводить его вообще
# - Фильтровать выходы (в ручную, ignore_items)
# - Разные товары 999999
# %% [markdown]
# ### Задание 1. Weighted Random Recommendation
# 
# Напишите код для случайных рекоммендаций, в которых вероятность рекомендовать товар прямо пропорциональна логарифму продаж
# - Можно сэмплировать товары случайно, но пропорционально какому-либо весу
# - Например, прямопропорционально популярности. вес = log(sales_sum товара)
# - Придумайте пример 3 весов, посчитайте weighted_random_recommendation для разных весов

# %%
def weighted_random_recommendation(items_weights, n=5):
    """Случайные рекоммендации
    
    Input
    -----
    items_weights: pd.DataFrame
        Датафрейм со столбцами item_id, weight. Сумма weight по всем товарам = 1
    """
    
    #! реализовал через клас WeightRandomRecommendation
    #! код разместил только для примера
    recs = np.random.choice(
            items_weights['item_id'], 
            replace=False,
            p=items_weights['weights'], 
            size=n)
    
    return recs.tolist()


# %%
get_ipython().run_cell_magic('time', '', "\nfrom Recommendation_systems.hw2.baseline import WeightRandomRecommendation\nmodel = WeightRandomRecommendation(\n    item_tag='item_id',\n    weight_tag='sales_sum'\n)\n# расчитаем потраченые деньги на каждый товар\ndata_train['sales_sum'] = data_train['quantity']*data_train['sales_value'] \nmodel.fit(data_train)\nmodel.recommend()")

# %% [markdown]
# ### Сделайте предсказания
# %% [markdown]
# #### Weight Random Recommendation
# %% [markdown]
# ### Задание 2. Расчет метрик
# Рассчитайте Precision@5 для каждого алгоритма (с вебинара и weighted_random_recommendation) с помощью функции из вебинара 1. Какой алгоритм показывает лучшее качество? Почему?

# %%
result = pd.read_csv('Recommendation_systems/hw2/preds.csv')# закгрузка predict с семианара
result.head(2)

# %%
type(result['actual'][0])


# %%
# файл с предсказаниями сохранил предсказания как строки
# нужно перевести обратно в список
for a in result.columns[1:]:
    result.loc[:, a]=  result[a].map(lambda x: x[1:-1].split(', ')).apply(lambda x: list(map(int, x)))


# %%
type(result['own_purchases'][0])

# %%
result['weight_random_recommendation'] = result['user_id'].apply(lambda user_id: model.recommend())
result.head(2)

# %%
def precision_at_k(recommended_list, bought_list, k=5):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]
    
    flags = np.isin(bought_list, recommended_list)
    precision = flags.sum() / len(recommended_list)
    
    
    return precision


# %%
result.apply(lambda x: precision_at_k(x['own_purchases'], x['actual'],  5), axis=1).mean()

#%%
from Recommendation_systems.hw2.metric import MetricManager

metrics = MetricManager()
for index in result.index:
    item = result.iloc[index]
    if len(item['random_recommendation'])==5:
        metrics.apply(        
            recommended = item['random_recommendation'],
            boughted = item['actual'],
            name = 'random_recommendation',
            user = item['user_id']
            )
    if len(item['popular_recommendation'])==5:
        metrics.apply(        
            recommended = item['popular_recommendation'],
            boughted = item['actual'],
            name = 'popular_recommendation',
            user = item['user_id']
            )
    if len(item['itemitem'])==5:
        metrics.apply(        
            recommended = item['itemitem'],
            boughted = item['actual'],
            name = 'itemitem',
            user = item['user_id']
            )
    if len(item['cosine'])==5:
        metrics.apply(        
            recommended = item['cosine'],
            boughted = item['actual'],
            name = 'cosine',
            user = item['user_id']
            )
    if len(item['tfidf'])==5:
        metrics.apply(        
            recommended = item['tfidf'],
            boughted = item['actual'],
            name = 'tfidf',
            user = item['user_id']
            )
    if len(item['own_purchases'])==5:
        metrics.apply(        
            recommended = item['own_purchases'],
            boughted = item['actual'],
            name = 'own_purchases',
            user = item['user_id']
            )
    if len(item['weight_random_recommendation'])==5:
        metrics.apply(        
            recommended = item['weight_random_recommendation'],
            boughted = item['actual'],
            name = 'weight_random_recommendation',
            user = item['user_id']
            )
metrics.show_table()

# %% [markdown]
# ### Задание 3. Улучшение бейзлайнов и ItemItem
# 
# - Попробуйте улучшить бейзлайны, считая их на топ-5000 товаров
# - Попробуйте улучшить разные варианты ItemItemRecommender, выбирая число соседей $K$.
# - Попробуйте стратегии ансамблирования изученных алгоритмов
# 

# %%
# your_code

# %% [markdown]
# ### Задание 4*. Улучшение детерминированных алгоритмов
# На семинаре мы рассматривали 
# 
# 
# %% [markdown]
# Далее $U \equiv N_i(u) $
# 
# $$r_{u,i} =  \frac{1}{S}\sum\limits_{v \in U}\operatorname{sim}(u,v)r_{v, i}$$
# $$ S = \sum\limits_{v \in U} \operatorname{sim}(u,v)$$
# 
# Предлагается улучшить эту формулу и учесть средние предпочтения всех пользователей
# 
# $$r_{u,i} = \mu + \bar{r_u} + \frac{1}{S}\sum\limits_{v \in U}\operatorname{sim}(u,v)(r_{v, i}-\bar{r_{v}} - \mu)$$
# %% [markdown]
# Какие смысл имееют $ \mu $ и $ \bar{r_u}$ ?
# 
# Реализуйте алгоритм, прогнозирующий рейтинги на основе данной формулы, на numpy (векторизованно!)
# 
# В качестве схожести возьмите CosineSimilarity.
# 
# Примените к user_item_matrix. В качестве рейтингов возьмите количество или стоимость купленного товара. 
# Данный алгоритм предсказывает рейтинги. Как на основании предсказанных рейтингов предсказать факт покупки?
# 
# Предложите вариант.
# Посчитайте accuracy@5 и сравните с алгоритмами, разобранными на вебинаре.

