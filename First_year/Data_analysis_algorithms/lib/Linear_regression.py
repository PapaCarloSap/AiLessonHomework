import numpy as np
import Data_analysis_algorithms.lib.data_analysis_lib as dal


class LinearRegression:
  
    def __init__(self):
        pass

    def fit_model(self,
        X: np.array,                    # Матрица признаков для обучения.
        y: np.array,                    # Вектор целевой переменной для обучения.
        learning_rate: float = 0.01,    # Скорость обучения.   
        n_iters: int = 100000,          # Количество итераций обучения.
        tol: float = 1e-5               # Минимальное значимое изменение ошибки, при котором обучение продолжается.
        ):
        """
        Обучение линейной регрессии алгоритмом градиентного спуска.

        Parameters
        ----------
        X: np.array
            Матрица признаков для обучения.

        y: np.array
            Вектор целевой переменной для обучения.

        learning_rate: float, optional, default = 0.01
            Скорость обучения. Опциональный параметр, по
            умолчанию, равен 0.01.

        n_iters: int, optional, default = 1000
            Количество итераций обучения. Опциональный параметр,
            по умолчанию, равен 1000.

        tol: float, optional, default = 1e-5
            Минимальное значимое изменение ошибки, при котором
            обучение продолжается. Если изменение ошибки на соседних
            итерациях меньше указанной величины, то обучение прекращается.

        Returns
        -------
        weights: np.array
            Вектор весов линейной модели.

        weights_history: List[np.array]
            Список с векторами весов на каждой итерации обучения.

        errors_history: List[float]
            Список со значением ошибки на каждой итерации обучения.

        """
        weights = np.random.randn(X.shape[0])
        errors_history, weights_history = [], [weights]

        for n_iter in range(n_iters):
            y_pred = np.dot(weights, X)
            current_error = dal.calc_mse(y, y_pred)
            weights = weights - 2*learning_rate*np.sum(X*(y_pred - y), axis=1)/len(y_pred)
            # weights = weights - 2*learning_rate*np.dot(X, (y_pred-y))/len(y_pred)
            errors_history.append(current_error)
            weights_history.append(weights)

            if n_iter > 2 and np.abs(current_error - errors_history[-2]) < tol:
                break
            
        return weights, weights_history, errors_history
