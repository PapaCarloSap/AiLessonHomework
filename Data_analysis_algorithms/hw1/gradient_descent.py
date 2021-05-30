# from Data_analysis_algorithms.hw1.data_analysis_lib import calc_mse
import numpy as np


class GradientDescentModel:
    
    weights_history = []
    current_weights

    def __init__(self):
        pass

    def fit(self, 
        X:np.array,                     # Матрица признаков для обучения.
        y:np.array,                     # Вектор целевой переменной для обучения.
        learning_rate: float = 0.01,    # Скорость обучения. Опциональный параметр, по умолчанию, равен 0.01.
        n_iters: int = 100000,          # Количество итераций обучения. Опциональный параметр, по умолчанию, равен 1000.
        tol: float = 1e-5              # Минимальное значимое изменение ошибки, при котором обучение продолжается.
         ):

        weights = np.random.randn(X.shape[0])
        errors_history, weights_history = [], [weights]

        for n_iter in range(n_iters):
            y_pred = np.dot(weights, X)
            current_error = calc_mse(y, y_pred)
            weights = weights - 2*learning_rate*np.sum(X*(y_pred - y), axis=1)/len(y_pred)
            # weights = weights - 2*learning_rate*np.dot(X, (y_pred-y))/len(y_pred)
            errors_history.append(current_error)
            weights_history.append(weights)

            if n_iter > 2 and np.abs(current_error - errors_history[-2]) < tol:
                break
        
        return weights, weights_history, errors_history
