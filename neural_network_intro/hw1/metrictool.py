from collections.abc import Sized, Iterable, Iterator
from typing import Dict,  List, Tuple
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import seaborn as sns

class Experiment:
    def __init__(self, name:str, errors:np.array, run_time:float):
        self.__name = name
        self.__errors = errors
        self.__run_time = run_time

    @property
    def name(self)->str:
        return self.__name

    @property
    def errors(self)->np.array:
        return self.__errors
        
    @property
    def run_time(self)->np.array:
        return self.__run_time

    def get_accuracy(self)->str:
        return str(round((1 - self.__errors[-1]) * 100,2)) + "%"

    def get_time_execution(self)->str:
        return "%.5s sec"% self.__run_time

    def add_fit_progress(self, ax:Axes):
        ax.plot(self.__errors, label=f'{self.__name}: accur:{self.get_accuracy()} time:{self.get_time_execution()}', lw=2, alpha=.8)

class ExperimentRepository(Sized,Iterator[Experiment]):
    
    __repo = dict()

    def __init__(self) -> None:
        pass

    def __iter__(self)-> Iterator[Experiment]:
        return iter(self.__repo.items())

    def __next__(self)->Tuple[int, Experiment]:
        return next(iter(self.__repo.items()))
        return next(self.__repo)

    def __len__(self) -> int:
        return len(self.__repo)

    def __getitem__(self, key:str) -> Experiment:
        return self.__repo.get(key)

    def append(self, name:str, experement: Experiment):
        self.__repo.update({name:experement})

class MetricRegressionManager:

    def __init__(self):
        self.__repo = ExperimentRepository() 

    def apply(self, name:str, errors: np.array, run_time: float):
        self.__repo.append(name, Experiment(name, errors, run_time))

    def show_report(self):
        self.__show_fit_progress()
        self.__show_table_report()

    def __short_format(self, value: float):
        return '%.3f' % (value)

    def show_table_report(self):   
        self.__show_table_report()

    def __show_table_report(self):
        table = list()
        experiment:Experiment = None
        for name, experiment in self.__repo:
            table.append([
                name,
                experiment.get_accuracy(),
                experiment.get_time_execution()              
            ])
        print(tabulate(table, headers=['Name model','Accuracy', 'Time']))

    def __show_fit_progress(self):
        fig, ((ax1)) = plt.subplots(1, 1,figsize=(12,5))
        fig.suptitle('Прогресс обучения', fontsize=16)
        experiment:Experiment = None
        for name, experiment in self.__repo:
            experiment.add_fit_progress(ax1)
        ax1.legend(loc="upper right")
        fig.tight_layout()
        plt.show()