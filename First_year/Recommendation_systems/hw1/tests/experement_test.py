import numpy as np
from numpy.testing import assert_almost_equal
import pytest
from Recommendation_systems.hw1.helpers_lib import Experement

prices = {
    1: 10,
    2: 20,
    3: 30,
    4: 15,
    5: 25,
    6: 35,
    7: 60,
    8: 50,
    9: 40,
    10: 65,
    11: 55,
    12: 45,
    }

@pytest.fixture()
def experement_init():
    from Recommendation_systems.hw1.helpers_lib import Experement
    return (
        Experement(
            recommended =   np.array([2, 5, 7, 4, 11, 9, 8, 10, 12, 3]),
            boughted =      np.array([1, 3, 5, 7, 9, 11])
            )

    )

def test_experement_hit_rate(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.hit_rate()
    # assert    
    assert True == result, 'Incorrectly defined Hit rate'

def test_experement_hit_rate_k(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.hit_rate_at_k(k=3)
    # assert    
    assert True == result, 'Incorrectly defined Hit rate for k = 3'

def test_experement_hit_rate_k_1(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.hit_rate_at_k(k=1)
    # assert    
    assert False == result, 'Incorrectly defined Precisionfor k = 1'

def test_experement_precision(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.precision()
    # assert    
    assert 0.5 == result

def test_experement_precision_at_k(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.precision_at_k(k=3)
    # assert    
    assert assert_almost_equal(0.66, result, decimal=2)==None

def test_experement_money_precision_at_k(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.money_precision_at_k(
        prices_recommended=[20, 3, 7, 30, 11, 50, 8, 25, 12, 33],
        k=3)
    # assert    
    assert assert_almost_equal(0.37, result, decimal=2)==None

def test_experement_recall(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.recall()
    # assert    
    assert assert_almost_equal(0.83, result, decimal=2)==None

def test_experement_recall_at_k(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.recall_at_k(k=3)
    # assert    
    assert assert_almost_equal(0.33, result, decimal=2)==None

def test_experement_money_recall_at_k(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.money_recall_at_k(
        prices=prices,
        k=3)
    # assert    
    assert assert_almost_equal(0.386, result, decimal=3)==None
    
def test_experement_ap_k(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.ap_k(k=3)
    # assert    
    assert assert_almost_equal(result, 0.116, decimal=3)==None
    
def test_experement_dcg_k(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.dcg_k(k=3)
    # assert    
    assert assert_almost_equal(result, 0.597, decimal=3)==None
    
def test_experement_ndcg_k(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.ndcg_k(k=3)
    # assert    
    assert assert_almost_equal(result, 0.641, decimal=3)==None

def test_experement_mrr(experement_init:Experement):
    experement = experement_init
    # act
    result = experement.mrr(k=3)
    # assert    
    assert assert_almost_equal(result, 0.277, decimal=3)==None