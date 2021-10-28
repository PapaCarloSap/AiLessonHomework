# %%
from IPython import get_ipython

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')

#%%
# генерации случайных чисел для инициализации весов
np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1

w1 = 2 * np.random.random((1, 2)) - 1
w2 = 2 * np.random.random((2, 2)) - 1
# %%
# генерации случайных чисел для инициализации весов
np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1


# вычисление сигмоид функции
def sigmoid(x):
     return 1 / (1 + np.exp(-x))

# вычисление производной от сигмоид функции
def sigm_deriv(x):
        return x * (1 - x)
    
# вычисление Relu функции

def ReLU(x):
         return x  *  (x  >  0)
# вычисление производной от Relu функции
def relu_deriv(x):
    return x>0

#%%
# для картинки
D  = 10

X = np.linspace(0-D,0+D,210)
Y = sigmoid(X)
dY = sigm_deriv(sigmoid(X))

plt.figure(figsize =(16,4))
plt.subplot(1,2,1)
plt.plot(X ,  Y ,'-g',label = 'сигмоид' )
plt.plot(X ,  dY ,'-r',label = 'd сигмоид' )
plt.grid('On')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

Yr = ReLU(X)
dYr = relu_deriv(ReLU(X))
plt.subplot(1,2,2)
plt.plot(X ,  Yr ,'-g',label = 'ReLU' )
plt.plot(X ,  dYr ,'-r',label = 'd ReLU' )
plt.legend()
plt.grid('On')
plt.xlabel('X')
plt.ylabel('Yr')
plt.show()

#%%
def train_nn(training_inputs, training_outputs, training_iterations):
    global synaptic_weights
    for iteration in range(training_iterations):
        # перекачивание данных через нейрон
        output = run_nn(training_inputs)

        # вычисление ошибки через обратное распространение back-propagation
        error = training_outputs - output
            
        # выполнение корректировки весов
        adjustments = np.dot(training_inputs.T, error * sigm_deriv(output))

        synaptic_weights += adjustments


# пропускание входных данных через нейрон и получение предсказания
# конвертация значений во floats
def run_nn(inputs):
    global synaptic_weights
    inputs = inputs.astype(float)
    output = sigmoid(np.dot(inputs, synaptic_weights))
    return output

#%%
# создание данных для обучения
training_inputs = np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
training_outputs = np.array([[0,1,1,0]]).T

# запуск тренировки нейронной сети 
train_nn(training_inputs, training_outputs, 1000)
print("веса после завершения обучения: ")
print(synaptic_weights)

# получение трех чисел от пользователя
# user_inp1 = str(input("Первое число(0 или 1): "))
# user_inp2 = str(input("Второе число(0 или 1): "))
# user_inp3 = str(input("Третье число(0 или 1): "))

# print("Проверка на новых данных: {user_inp1} {user_inp2} {user_inp3}")
# print("Предсказание нейронной сети: ")
# print(run_nn(np.array([user_inp1, user_inp2, user_inp3])))

#%%
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#%%
### Шаг 1. Определение функций, которые понадобяться для обучения
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

# сигмоида и ее производная
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_deriv(x):
    return (x)*(1 - (x))

# нормализация массива
def normalize(X, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(X, order, axis))
    l2[l2 == 0] = 1
    return X / np.expand_dims(l2, axis)

#%%

### Шаг 2. Подготовка тренировочных данных
# получения данных из csv файла. укажите здесь путь к файлу Iris.csv
TARGET = 'target'
iris = load_iris()
iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
iris_df[TARGET].astype(int)

# репрезентация данных в виде графиков
g = sns.pairplot(iris_df, hue=TARGET)

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
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

#%%
### Шаг 3. Обученние нейронной сети

# определим число нейронов скрытого слоя
neuron_numb = 2


# присваевание случайных весов



w0 = 2*np.random.random((4, neuron_numb)) - 1 # для входного слоя   - 4 входа, 3 выхода
w1 = 2*np.random.random((neuron_numb, 3)) - 1 # для внутреннего слоя - 5 входов, 3 выхода

# скорость обучения (learning rate)
n = 0.05

# массив для ошибок, чтобы потом построить график
errors = []

# процесс обучения
for i in range(10000):

    # прямое распространение(feed forward)
    layer0 = X_train
    layer1 = sigmoid(np.dot(layer0, w0))
    layer2 = sigmoid(np.dot(layer1, w1))

    # обратное распространение(back propagation) с использованием градиентного спуска
    layer2_error = y_train - layer2 # производная функции потерь = производная квадратичных потерь 
    layer2_delta = layer2_error * sigmoid_deriv(layer2)
    
    layer1_error = layer2_delta.dot(w1.T)
    layer1_delta = layer1_error * sigmoid_deriv(layer1)
    # коррекция
    w1 += layer1.T.dot(layer2_delta) * n
    w0 += layer0.T.dot(layer1_delta) * n
    # метрика модели
    error = np.mean(np.abs(layer2_error))
    errors.append(error)
    accuracy = (1 - error) * 100

### Шаг 4. Демонстрация полученных результатов
# черчение диаграммы точности в зависимости от обучения
plt.figure(figsize = (16,5))
plt.plot(errors)
plt.xlabel('Обучение')
plt.ylabel('Ошибка')
plt.show() # расскоментируйте, чтобы посмотреть 

N = 50
plt.figure(figsize = (16,5))
plt.plot(layer2[:N,1], 'r',label = 'Y new')
plt.plot(y_train[:N,1],'g', label = 'Y train')
plt.xlabel('№ примера')
plt.ylabel('выход сети и целевой')
plt.legend( )
plt.show() # расскоментируйте, чтобы посмотреть 
        
print("Аккуратность нейронной сети " + str(round(accuracy,2)) + "%")

#%%
from hw1.model import Model
from hw1.layerlib import StartLayer, HiddenLayer, FinishLayer
from hw1.activationlib import Sigmoid, ReLU
from hw1.metrictool import MetricRegressionManager

#%%
learning_rate_fit_metric = MetricRegressionManager()

#%%
model = Model(
        layer_map=[
            StartLayer(neuron=4),
            HiddenLayer(neuron=5, activation=Sigmoid()),
            FinishLayer(neuron=3, activation=Sigmoid())
        ],
        epoch_num=10000,
        learning_rate=0.05
    )
errors, run_time = model.fit(X_train, y_train)
learning_rate_fit_metric.apply(
    str(model),
    errors,
    run_time
    )

model = Model(
        layer_map=[
            StartLayer(neuron=4),
            HiddenLayer(neuron=5, activation=Sigmoid()),
            FinishLayer(neuron=3, activation=Sigmoid())
        ],
        epoch_num=10000,
        learning_rate=0.10
    )
errors, run_time = model.fit(X_train, y_train)
learning_rate_fit_metric.apply(
    str(model),
    errors,
    run_time
    )

learning_rate_fit_metric.show_report()

#%%
epoch_fit_metric = MetricRegressionManager()

model = Model(
        layer_map=[
            StartLayer(neuron=4),
            HiddenLayer(neuron=5, activation=Sigmoid()),
            FinishLayer(neuron=3, activation=Sigmoid())
        ],
        epoch_num=10000,
        learning_rate=0.05
    )
errors, run_time = model.fit(X_train, y_train)
epoch_fit_metric.apply(
    str(model),
    errors,
    run_time
    )

model = Model(
        layer_map=[
            StartLayer(neuron=4),
            HiddenLayer(neuron=5, activation=Sigmoid()),
            FinishLayer(neuron=3, activation=Sigmoid())
        ],
        epoch_num=100,
        learning_rate=0.05
    )
errors, run_time = model.fit(X_train, y_train)
epoch_fit_metric.apply(
    str(model),
    errors,
    run_time
    )

model = Model(
        layer_map=[
            StartLayer(neuron=4),
            HiddenLayer(neuron=5, activation=Sigmoid()),
            FinishLayer(neuron=3, activation=Sigmoid())
        ],
        epoch_num=1000,
        learning_rate=0.05
    )
errors, run_time = model.fit(X_train, y_train)
epoch_fit_metric.apply(
    str(model),
    errors,
    run_time
    )

epoch_fit_metric.show_report()

#%%