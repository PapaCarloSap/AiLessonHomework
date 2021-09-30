import numpy as np
from abc import ABC, ABCMeta, abstractmethod

class Activation(ABC):

    @abstractmethod
    def func(self, x:np.array)->np.array:
        ...

    @abstractmethod
    def derivative(self, x:np.array)->np.array:
        ...

    def __str__(self):
        return self.__name__

class Sigmoid(Activation):
    """Сигмойда"""

    def func(self, x:np.array)->np.array:
        return 1 / (1 + np.exp(-x))

    def derivative(self, x:np.array)->np.array:
        return x * (1 - x)

    def __str__(self):
        return "sig"

class ReLU(Activation):
    """ReLU"""

    def func(self, x:np.array)->np.array:
        return x  *  (x  >  0)

    def derivative(self, x:np.array)->np.array:
        return x>0

    def __str__(self):
        return "relu"