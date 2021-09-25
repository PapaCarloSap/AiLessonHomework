import pandas as pd
import numpy as np
import pytest

# Определение функций, которые понадобяться для обучения
# преобразование массива в бинарный вид результатов
def to_one_hot(Y):
    n_col = np.amax(Y) + 1
    binarized = np.zeros((len(Y), n_col))
    for i in range(len(Y)):
        binarized[i, Y[i]] = 1.
    return binarized

# преобразование массива в необходимый вид
def from_one_hot(Y):
    arr = np.zeros((len(Y), 1))

    for i in range(len(Y)):
        l = Y[i]
        for j in range(len(l)):
            if(l[j] == 1):
                arr[i] = j+1
    return arr

def normalize(X, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(X, order, axis))
    l2[l2 == 0] = 1
    return X / np.expand_dims(l2, axis)

@pytest.fixture()
def iris():
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris  

    # Подготовка тренировочных данных
    # получения данных из csv файла. укажите здесь путь к файлу Iris.csv
    TARGET = 'target'
    iris = load_iris()
    iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                        columns= iris['feature_names'] + ['target'])
    iris_df[TARGET].astype(int)

    x = iris_df.drop(columns=[TARGET])
    #x = normalize(x.as_matrix())
    x = normalize(x.values)

    # формирование выходных данных(результатов)
    y = pd.DataFrame(iris_df[TARGET], columns=[TARGET])
    #y = y.as_matrix()
    y = y.values
    y = y.flatten()
    y = to_one_hot(y.astype(int))

    # Разделение данных на тренировочные и тестовые
    yield train_test_split(x, y, test_size=0.33) #X_train, X_test, y_train, y_test

def test_model(iris):
    from hw1.model import Model
    from hw1.layerlib import StartLayer, HiddenLayer, FinishLayer
    from hw1.activationlib import Sigmoid
    model = Model(
        layer_map=[
            StartLayer(neuron=4),
            HiddenLayer(neuron=2, activation=Sigmoid()),
            FinishLayer(neuron=3, activation=Sigmoid())
        ],
        epoch_num=1000,
        learning_rate=0.05
    )
    errors, run_time = model.fit(x_train=iris[0], y_train=iris[2])
    print("--- %s seconds ---" % run_time)
    assert len(errors)>0