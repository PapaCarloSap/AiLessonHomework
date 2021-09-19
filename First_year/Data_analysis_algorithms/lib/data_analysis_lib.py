import numpy as np


def calc_mse(y_true: np.array, y_pred: np.array) -> float:
    """
    Вычисление значение метрики MSE (Mean-Squared-Error).
    http://kb.local:8090/pages/viewpage.action?pageId=34439206

    Parameters
    ----------
    y_true: np.array
        Вектор истинных ответов.

    y_pred: np.array
        Вектор прогнозов.

    Returns
    -------
    score: float
        Значение метрики качества.

    """
    assert len(y_true) == len(y_pred)
    return np.mean((y_true-y_pred)**2)

def calc_mae(y_true: np.array, y_pred: np.array) -> float:
    """
    Вычисление значение метрики MAE (Mean absolute error).
    http://kb.local:8090/pages/viewpage.action?pageId=34439206

    Parameters
    ----------
    y_true: np.array
        Вектор истинных ответов.

    y_pred: np.array
        Вектор прогнозов.

    Returns
    -------
    score: float
        Значение метрики качества.

    """
    assert len(y_true) == len(y_pred)
    return np.mean(np.abs(y_true-y_pred))

def calc_rmse(y_true: np.array, y_pred: np.array) -> float:
    """
    Вычисление значение метрики RMSE (Root Mean Square Error).
    http://kb.local:8090/pages/viewpage.action?pageId=34439206

    Parameters
    ----------
    y_true: np.array
        Вектор истинных ответов.

    y_pred: np.array
        Вектор прогнозов.

    Returns
    -------
    score: float
        Значение метрики качества.

    """
    assert len(y_true) == len(y_pred)
    return np.sqrt(calc_mse(y_true, y_pred))