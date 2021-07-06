import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import f1_score, roc_auc_score, precision_score, classification_report, precision_recall_curve, confusion_matrix


class MetricRegressionManager:

    def __init__(self):
        self.__repo = ExperimentRepository() 

    def apply(self, name:str, y_source: np.array, y_pred: np.array):
        self.__repo.append({name: self.Experiment(name, y_source, y_pred)})

    def calc_metric(self, name:str, show=False)->tuple():
        result = self.__repo[str].get_precision_recall_curve()
        if show:
            print('Best Threshold=%.3f, F-Score=%.3f, Precision=%.3f, Recall=%.3f' % result)
        return result

    def calc_metric(self):   
        for experiment in self.__repo:
            print('Best Threshold=%.3f, F-Score=%.3f, Precision=%.3f, Recall=%.3f' % experiment.get_precision_recall_curve())
            

class Experiment:
            
    def __init__(self, name:str, source:np.array, pred:np.array):
        self.name = name
        self.source = source
        self.pred = pred

    @property
    def name(self)->str:
        return self.name

    @property
    def source(self)->np.array:
        return self.source
        
    @property
    def pred(self)->np.array:
        return self.pred

    def get_precision_recall_curve(self)->tuple():
        precision, recall, thresholds = precision_recall_curve(self.source, self.pred)
        fscore = (2 * precision * recall) / (precision + recall)
        # locate the index of the largest f score
        ix = np.argmax(fscore)
        return thresholds[ix], fscore[ix], precision[ix], recall[ix]

class ExperimentRepository:
    
    repo = dict()

    def __init__(self) -> None:
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.repo)

    def __len__(self) -> int:
        return len(self.repo)

    def __getitem__(self, key:str) -> Experiment:
        return self.repo[key]

