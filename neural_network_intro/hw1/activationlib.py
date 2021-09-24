import numpy as np
from abc import ABC, ABCMeta, abstractmethod

class Activation(ABC):
    @abstractmethod
    def func(self, x:np.array)->np.array:
        ...

    @abstractmethod
    def derivative(self, x:np.array)->np.array:
        ...

class Sigmoid(Activation):
    """Сигмойда"""
    
    def func( x:np.array)->np.array:
        return 1 / (1 + np.exp(-x))

    def derivative(x:np.array)->np.array:
        return x * (1 - x)

class ReLU(Activation):
    """ReLU"""

    def func(x:np.array)->np.array:
        return x  *  (x  >  0)

    def derivative(x:np.array)->np.array:
        return x>0