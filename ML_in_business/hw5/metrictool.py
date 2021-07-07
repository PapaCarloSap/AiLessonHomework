from tokenize import Name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from sklearn import metrics
from sklearn.metrics import f1_score, roc_auc_score, precision_score, classification_report, precision_recall_curve, confusion_matrix
from tabulate import tabulate
from deprecated import deprecated


class Metric:
    def __init__(self, thresholds, fscore, precision, recall, roc_auc):
        self.__thresholds = thresholds
        self.__fscore = fscore
        self.__precision = precision
        self.__recall = recall
        self.__roc_auc = roc_auc

    @property
    def Thresholds(self)->np.float:
        return self.__thresholds

    @property
    def Fscore(self)->np.float:
        return self.__fscore

    @property
    def Precision(self)->np.float:
        return self.__precision

    @property
    def Recall(self)->np.float:
        return self.__recall

    @property
    def Roc_AUC(self)->np.float:
        return self.__roc_auc

    def to_tuple(self):
        return self.__thresholds, self.__fscore, self.__precision, self.__recall

    def show_table(self):
        print(tabulate(
            [[
                self.Thresholds, self.Fscore, self.Precision, self.Recall, self.Roc_AUC
            ]],
            headers=['Threshold', 'F-Score', 'Precision', 'Recall', 'Roc-AUC'],
            floatfmt=(".3f",".3f",".3f",".3f",".3f")))


class Experiment:
    __metric = None

    def __init__(self, name:str, y_test:np.array, y_pred:np.array):
        self.__name = name
        self.__y_test = y_test
        self.__y_pred = y_pred

    @property
    def Name(self)->str:
        return self.__name

    @property
    def y_test(self)->np.array:
        return self.__y_test
        
    @property
    def y_pred(self)->np.array:
        return self.__y_pred

    def get_precision_recall_curve(self)->Metric:
        '''
        Переход от вероятностей к меткам классов. Для этого нужно подобрать порог, 
        после которого мы считаем, что объект можно отнести к классу 1 (если вероятность больше порога - 
        размечаем объект как класс 1, если нет - класс 0)
        Максимизируем по fscore
        '''

        precision, recall, thresholds = precision_recall_curve(self.__y_test, self.__y_pred)
        fscore = (2 * precision * recall) / (precision + recall)
        # locate the index of the largest f score
        ix = np.argmax(fscore)
        self.__metric = Metric(thresholds[ix], fscore[ix], precision[ix], recall[ix], roc_auc_score(self.__y_test, self.__y_pred))
        return self.__metric

    def get_confusion_matrix(self)->np.array:
        if self.__metric is None:
            self.get_precision_recall_curve()
        return confusion_matrix(self.__y_test, self.convert_probability_to_bin_by_thresholds(self.__metric.Thresholds))

    def get_profit(self) ->float:
        confusion_matrix = self.get_confusion_matrix()
        profit = 2 # 2 доллара за каждого правильно классифицированного (True Positive) удержанного пользователя
        expenses = 1 # 1 доллар на привлечение
        # confusion_matrix[0,:] - это те затраты которые мы понесли на привлечение
        return confusion_matrix[0,0]*profit - np.sum(confusion_matrix[0,:])*expenses

    @deprecated(reason='переработать в более гибкий для использования метод')
    def show_confusion_matrix(self):
        if self.__metric is None:
            self.get_precision_recall_curve()
        font = {'size' : 15}
        plt.rc('font', **font)
        cnf_matrix = confusion_matrix(self.__y_test, self.__y_pred>self.__metric.Thresholds)
        plt.figure(figsize=(10, 8))
        self.__plot_confusion_matrix(cnf_matrix, classes=['NonChurn', 'Churn'],
                            title='Confusion matrix')
        #plt.savefig("temp_conf_matrix.png")
        plt.show()

    def convert_probability_to_bin_by_thresholds(self, thresholds: float):
        # self.__y_pred>self.__thresholds - переход от вероятности к 1 и 0. thresholds - это порог перехода
        return self.__y_pred>thresholds

    @deprecated(reason='переработать в более гибкий для использования метод')
    def __plot_confusion_matrix(self, cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
        """
        Матрица ошибок
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        # print(cm)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

class ExperimentRepository:
    
    __repo = dict()

    def __init__(self) -> None:
        pass

    def __iter__(self):
        return iter(self.__repo.items())

    def __next__(self):
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

    def apply(self, name:str, y_test: np.array, y_pred: np.array):
        self.__repo.append(name, Experiment(name, y_test, y_pred))

    def calc_metric(self, name:str)->Metric:
        return self.__repo[name].get_precision_recall_curve()

    def __short_format(self, value: float):
        return '%.3f' % (value)

    def calc_metrics(self):   
        table = list()
        for name, experiment in self.__repo:
            metric = experiment.get_precision_recall_curve()
            table.append([
                name,
                self.__short_format(metric.Thresholds),
                self.__short_format(metric.Fscore),
                self.__short_format(metric.Precision),
                self.__short_format(metric.Recall),               
                self.__short_format(metric.Roc_AUC), 
                experiment.get_profit(),              
            ])
        print(tabulate(table, headers=['Name model','Threshold', 'F-Score', 'Precision', 'Recall', 'Roc-AUC', 'Profit $']))

    def get_confusion_matrix(self, name:str):
        self.__repo[name].get_confusion_matrix()

    def show_confusion_matrix(self, name:str):
        self.__repo[name].show_confusion_matrix()