import numpy as np
from enum import Enum
from typing import Dict, Tuple, List, cast
from hw1.layerlib import Layer, LayerRepository, StartLayer, HiddenLayer, FinishLayer, IBackPropagation
import time

class Model:
    def __init__(self, 
        layer_map:List[Layer],
        learning_rate:float = 0.05,
        epoch_num:int = 10000

    ):
        self.__weights:Dict[Layer, np.array] = dict()
        self.__layers = LayerRepository(layer_map)
        self.__learning_rate:float = learning_rate
        self.__epoch_num:int = epoch_num

    def __str__(self):
        return "type: {0}, ep:{1}, rate:{2}".format(
            str(self.__layers), 
            self.__epoch_num,
            self.__learning_rate
        )

    def __set_default_weight(self):
        """Сбрасываем веса на рандомные значения
        """
        self.__weights.clear()
        for order, layer in enumerate(self.__layers): 
            if type(layer) is FinishLayer: break
            self.__weights[layer.next_layer] = 2 * np.random.random((layer.neuron, layer.next_layer.neuron)) - 1

    def __prediction(self, input:np.array)->np.array:
        """Предсказание модели

        Returns:
            Tuple[int, Dict[int, float]]: 0 - предсказание, 1 - значение на слоях
        """
        last_layer_output_data = input
        for layer in self.__layers:
            if type(layer) is StartLayer: 
                layer.calc_output(last_layer_output_data)
            else:
                layer.calc_output(last_layer_output_data, self.__weights[layer])
            last_layer_output_data = layer.output_data    
        return last_layer_output_data 

    def predict_prob(self, input:np.array)->np.array:
        return self.__prediction(input)

    def fit(self, x_train:np.array, y_train:np.array):
        start_time = time.time()
        # присваевание случайных весов
        self.__set_default_weight()
        # процесс обучения
        errors = []
        back_propagation_layers:List[IBackPropagation] = [layer for layer in reversed(self.__layers) if issubclass(type(layer), IBackPropagation)] 
        for epoch in range(self.__epoch_num):
            # прямое распространение(feed forward)
            predict = self.__prediction(x_train)
            # обратное распространение(back propagation) с использованием градиентного спуска
            last_layer_delta:np.array = y_train
            for layer in back_propagation_layers:
                if type(layer) is FinishLayer: 
                    delta = layer.calc_delta(last_layer_delta, None)
                else:
                    delta = layer.calc_delta(last_layer_delta, self.__weights[layer.next_layer])
                last_layer_delta = delta
            # коррекция
            for layer, weight in self.__weights.items():
                self.__weights[layer] += layer.prev_layer.output_data.T.dot(layer.delta) * self.__learning_rate
            # метрика модели
            error = np.mean(np.abs(y_train-predict))
            errors.append(error)  
        return  errors, time.time() - start_time
