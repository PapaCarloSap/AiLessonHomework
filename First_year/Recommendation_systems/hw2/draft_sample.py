from typing import List
import numpy     as np
import pandas     as pd


def weighted_random_recommendation(items_weights, n=5)->List[np.array]:
    """Случайные рекоммендации
    
    Input
    -----
    items_weights: pd.DataFrame
        Датафрейм со столбцами item_id, weight. Сумма weight по всем товарам = 1
    """
    
    #items_weights = np.log(items_weights)
    recs = np.random.choice(items_weights['item_id'], p=items_weights['weighted'], size=n)
    
    return recs.tolist()

def sample1(data_train: pd.DataFrame):
    popularity = data_train.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    top_5000 = popularity.sort_values('n_sold', ascending=False).head(3).item_id.tolist()
    data_train.loc[~data_train['item_id'].isin(top_5000), 'item_id'] = 999999
    data_train.loc[data_train['item_id']==999999] = 0

def calc_by_sales_sum(df: pd.DataFrame)->pd.DataFrame:
    from Recommendation_systems.hw2.helper import WeightCoverter
    df['sales_sum'] = df['quantity']*df['sales_value'] 
    popularity = df.groupby('item_id')['sales_sum'].sum().reset_index()
    popularity['weighted'] = WeightCoverter(popularity['sales_sum']).get_weights()
    # coverter = WeightCoverter(popularity['sales_sum'])    
    # popularity['weighted'] = popularity['sales_sum'].apply(lambda x: coverter.get_weight(x))
    popularity['weighted_random_recommendation'] = weighted_random_recommendation(popularity[['item_id', 'weighted']])
    return popularity