import numpy as np
from hw1.activationlib import Activation
from abc import ABC, abstractmethod
from typing import Dict,  List, Tuple
from collections.abc import Sized, Iterable, Iterator

class Layer(ABC):
    def __init__(self, neuron:int)->None:
        self.__neuron:int = neuron
        self._output_data:np.array=None
        self._prev_layer:"Layer" = None
        self._next_layer:"Layer" = None

    @property
    def neuron(self)->int:
        return self.__neuron

    @property
    def output_data(self)->np.array:
        return self._output_data

    @property
    def prev_layer(self)->"Layer":
        return self._prev_layer

    @prev_layer.setter
    def prev_layer(self, layer:"Layer"):
        self._prev_layer = layer

    @property
    def next_layer(self)->"Layer":
        return self._next_layer

    @next_layer.setter
    def next_layer(self, layer:"Layer"):
        self._next_layer = layer

    @abstractmethod
    def calc_output(self, input:np.array, weight:np.array=None):
        ...

    def __str__(self):
        return self.__name__

class IBackPropagation():
    @abstractmethod
    def calc_error(self, expect_output:np.array, weight:np.array)->np.array:
        ...

    @abstractmethod
    def calc_delta(self, expect_output:np.array, weight:np.array)->np.array:
        ...

class StartLayer(Layer):
    def __init__(self,
            neuron:int 
        )->None:
        super().__init__(neuron=neuron)

    def calc_output(self, input:np.array, weight:np.array=None):
        self._output_data = input

    def __str__(self):
        return f"{self.neuron}"


class HiddenLayer(Layer, IBackPropagation):
    def __init__(self,
            neuron:int, 
            activation:Activation
        )->None:
        self.__delta:np.array = None
        super().__init__(neuron=neuron)
        self.__activation:Activation = activation

    @property
    def delta(self)->np.array:
        return self.__delta

    def calc_output(self, input:np.array, weight:np.array=None):
        self._output_data = self.__activation.func(np.dot(input, weight))

    def calc_error(self, expect_output:np.array, weight:np.array)->np.array:
        return expect_output.dot(weight.T)

    def calc_delta(self, expect_output:np.array, weight:np.array)->np.array:
        self.__delta = self.calc_error(expect_output, weight) * self.__activation.derivative(self._output_data)
        return self.__delta

    def __str__(self):
        return f"{self.neuron}{self.__activation}"

    
class FinishLayer(Layer, IBackPropagation):
    def __init__(self,
            neuron:int, 
            activation:Activation
        )->None:
        self.__delta:np.array = None
        super().__init__(neuron=neuron)
        self.__activation:Activation = activation

    @property
    def delta(self)->np.array:
        return self.__delta
    
    def calc_output(self, input:np.array, weight:np.array=None):
        self._output_data = self.__activation.func(np.dot(input, weight))

    def calc_error(self, expect_output:np.array, weight:np.array)->np.array:
        return expect_output - self._output_data

    def calc_delta(self, expect_output:np.array, weight:np.array)->np.array:
        self.__delta =  self.calc_error(expect_output, None) * self.__activation.derivative(self._output_data)
        return self.__delta

    def __str__(self):
        return f"{self.neuron}{self.__activation}"

class LayerRepository(Sized,Iterator[Layer]):
    def __init__(self, data:List[Layer]):
        self.__repo:Dict[int, Layer] = dict()
        prev_layer = None
        for key, layer in enumerate(data):
            if prev_layer is not None: prev_layer.next_layer = layer
            layer.prev_layer = prev_layer
            self.__repo.update({key:layer})
            prev_layer = layer
      
    def __iter__(self)-> Iterator[Layer]:
        for key, value in self.__repo.items():
            yield value
        #return iter(self.__repo.items())

    def __next__(self)->Tuple[int, Layer]:
        return next(iter(self.__repo.items()))

    def __len__(self) -> int:
        return len(self.__repo)

    def __getitem__(self, number:int) -> Layer:
        return self.__repo.get(number)

    def __str__(self):
        result:str = ''
        for key, layer in self.__repo.items():
            result += f'{str(layer)}x'
        return result[:-1]

    # def append(self, number:int, experement: Layer):
    #     self.__repo.update({number:experement})
