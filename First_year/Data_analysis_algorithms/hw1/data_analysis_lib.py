import numpy as np


def calc_mse(y:np.ndarray, y_pred:np.ndarray):
    return np.mean((y-y_pred)**2)

def calc_mae(y:np.ndarray, y_pred:np.ndarray):
    return np.mean(np.abs(y-y_pred))

def calc_rmse(y:np.ndarray, y_pred:np.ndarray):
    return np.sqrt(calc_mse(y, y_pred))