import numpy as np
import pandas     as pd


def test_weighted_random_recommendation():
    from Recommendation_systems.hw2.draft_sample import weighted_random_recommendation
    arr = [1,2,3,4,5,6]
    result = weighted_random_recommendation(arr)
    assert True

def test_sample1():
    from Recommendation_systems.hw2.draft_sample import sample1
    df = pd.DataFrame({ 
        'item_id'   :   [1,2,3,4,5,1],
        'quantity'  :   [1,1,0,1,0,3],
        'sales_val' :   [5,4,3,2,1,5],
        })
    sample1(df) 
    assert True

def test_sales_sum():
    from Recommendation_systems.hw2.draft_sample import calc_by_sales_sum
    df = pd.DataFrame({ 
        'item_id'       :   [1,2,3,4,5,1],
        'quantity'      :   [1,1,0,1,0,3],
        'sales_value'   :   [5,4,3,2,1,5],
        })
    result = calc_by_sales_sum(df)
    assert True