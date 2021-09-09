from tokenize import Name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import itertools
from sklearn import metrics
from sklearn.metrics import f1_score, roc_auc_score, precision_score, precision_recall_curve, confusion_matrix, recall_score, roc_curve, auc
from tabulate import tabulate
from deprecated import deprecated
from typing import List, Dict


class ConfusionMatrix:
    def __init__(self, y_test:np.array, y_pred:np.array) -> None:
        self.__y_test = y_test
        self.__y_pred = y_pred
        self.__calc_confusion_matrix()

    @property
    def Value(self)->np.array:
        return self.__value

    # --

    @property
    def TN(self)->int:
        return self.__value[0][0]

    @property
    def FN(self)->np.array:
        return self.__value[1][0]

    @property
    def TP(self)->np.array:
        return self.__value[1][1]

    @property
    def FP(self)->np.array:
        return self.__value[0][1]

    # --

    @property
    def TPR(self)->np.array:
        return self.TP/(self.TP+self.FN)

    @property
    def FPR(self)->np.array:
        return self.FP/(self.FP+self.TN)

    @property
    def TNR(self)->np.array:
        return self.TN/(self.FP+self.TN)

    @property
    def Precision(self)->np.array:
        return self.TP/(self.TP+self.FP)

    @property
    def Recall(self)->np.array:
        return self.TPR


    @property
    def Accuracy(self)->np.array:
        return (self.TP + self.TN)/(self.TP + self.TN + self.FP + self.FN)  

    def get_f1score(self, b:float=1)->np.array:
        return (1 + b*b) * self.Precision * self.Recall / ((b*b*self.Precision) + self.Recall)

    @deprecated(reason='переработать в более гибкий для использования метод')
    def show_picture(self, 
        title:str = 'Confusion matrix',
        name_positive:str = '0', 
        name_negative:str = '1', 
    ):
        font = {'size' : 15}
        plt.rc('font', **font)
        plt.figure(figsize=(10, 8))
        self.__plot_confusion_matrix(self.__value, classes=[name_positive, name_negative],
                            title=title)
        #plt.savefig("temp_conf_matrix.png")
        plt.show()

    def __calc_confusion_matrix(self):
        self.__value = confusion_matrix(self.__y_test, self.__y_pred)

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
        plt.ylabel('Фактические значения')
        plt.xlabel('Спрогнозированые значения')

    def show_metric(self):
        print(tabulate(
            [[
                self.TPR, self.FPR, self.TNR, self.Precision, self.Recall, self.Accuracy
            ]],
            headers=['TPR', 'FPR', 'TNR', 'Precision', 'Recall', 'Accuracy'],
            floatfmt=(".3f",".3f",".3f",".3f",".3f",".3f")))

    def show_table(self, 
        ax:Axes,
        title:str='Матрица ошибок', #'Confusion matrix',
        name_negative:str = '0', 
        name_positive:str = '1', 
        normalize:bool=False
    ):
        ax.grid(False)
        ax.yaxis.set_major_locator(plt.NullLocator())
        ax.xaxis.set_major_formatter(plt.NullFormatter())
        classes=[name_positive, name_negative]
        cmap=plt.cm.Blues
        ax.imshow(self.__value, interpolation='nearest', cmap=cmap)
        ax.set_title(title)
        ax.text(-0.5, 0, name_negative, fontsize=10, horizontalalignment='center', verticalalignment='center', color='brown', rotation=90)
        ax.text(-0.5, 1, name_positive, fontsize=10, horizontalalignment='center', verticalalignment='center', color='brown', rotation=90)
        ax.text(0, 1.5, name_negative, fontsize=10, horizontalalignment='center', verticalalignment='center', color='brown')
        ax.text(1, 1.5, name_positive, fontsize=10, horizontalalignment='center', verticalalignment='center', color='brown')

        if normalize:
            cm = self.__value.astype('float') / self.__value.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            cm = self.__value
            print('Confusion matrix, without normalization')

        # print(cm)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            ax.text(j, i, cm[i, j],
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black")

        #ax.tight_layout()
        ax.set_ylabel('Фактические значения')
        ax.set_xlabel('Спрогнозированые значения')

class Metric:
    def __init__(self, thresholds, fscore, precision, recall, roc_auc, confusion_matrix:ConfusionMatrix):
        self.__thresholds = thresholds
        self.__fscore = fscore
        self.__precision = precision
        self.__recall = recall
        self.__roc_auc = roc_auc
        self.__confusion_matrix = confusion_matrix

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

    @property
    def Confusion_matrix(self)->ConfusionMatrix:
        return self.__confusion_matrix

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
        
    @property
    def metric(self)->Metric:
        return self.__metric

    def calc_metric(self, specified_thr:float = None)->Metric:
        '''
        Переход от вероятностей к меткам классов. Для этого нужно подобрать порог, 
        после которого мы считаем, что объект можно отнести к классу 1 (если вероятность больше порога - 
        размечаем объект как класс 1, если нет - класс 0)
        Максимизируем по fscore
        '''


        if specified_thr is None:
            precision, recall, thresholds = precision_recall_curve(self.__y_test, self.__y_pred)
            fscore = (2 * precision * recall) / (precision + recall)
            # locate the index of the largest f score
            ix = np.argmax(fscore)
            self.__metric = Metric(
                thresholds[ix], 
                fscore[ix], 
                precision[ix], 
                recall[ix], 
                roc_auc_score(self.__y_test, self.__y_pred), 
                confusion_matrix = self.__get_confusion_matrix(thresholds[ix]))
        else:
            confusion_matrix = self.__get_confusion_matrix(specified_thr)
            self.__metric = Metric(
                specified_thr, 
                confusion_matrix.get_f1score(), 
                confusion_matrix.Precision, 
                confusion_matrix.Recall, 
                roc_auc_score(self.__y_test, self.__y_pred), 
                confusion_matrix = confusion_matrix)

        return self.__metric

    def __get_confusion_matrix(self, thresholds)->ConfusionMatrix:
        return ConfusionMatrix(
            self.__y_test,
            self.__convert_probability_to_bin_by_thresholds(thresholds)
        )

    def __convert_probability_to_bin_by_thresholds(self, thresholds: float):
        # self.__y_pred>self.__thresholds - переход от вероятности к 1 и 0. thresholds - это порог перехода
        return self.__y_pred>thresholds

    def show_proba_calibration_plots(self,
        name_positive:str = 'Another class', # 0
        name_negative:str = 'Main class', # 1
        ):
        preds_with_true_labels = np.array(list(zip(self.__y_pred, self.__y_test)))

        thresholds = []
        precisions = []
        recalls = []
        f1_scores = []

        for threshold in np.linspace(0.1, 0.9, 9):
            thresholds.append(threshold)
            precisions.append(precision_score(self.__y_test, list(map(int, self.__y_pred > threshold))))
            recalls.append(recall_score(self.__y_test, list(map(int, self.__y_pred > threshold))))
            f1_scores.append(f1_score(self.__y_test, list(map(int, self.__y_pred > threshold))))

        scores_table = pd.DataFrame({'f1':f1_scores,
                                    'precision':precisions,
                                    'recall':recalls,
                                    'probability':thresholds}).sort_values('f1', ascending=False).round(3)
    
        figure = plt.figure(figsize = (15, 5))

        plt1 = figure.add_subplot(121)
        plt1.plot(thresholds, precisions, label='Precision', linewidth=2)
        plt1.plot(thresholds, recalls, label='Recall', linewidth=2)
        plt1.plot(thresholds, f1_scores, label='F1', linewidth=2)
        plt1.set_ylabel('Scores')
        plt1.set_xlabel('Probability threshold')
        plt1.set_title('Probabilities threshold calibration')
        plt1.legend(bbox_to_anchor=(0.25, 0.25))   
        plt1.table(cellText = scores_table.values,
                colLabels = scores_table.columns, 
                colLoc = 'center', cellLoc = 'center', loc = 'bottom', bbox = [0, -1.3, 1, 1])
        precision, recall, th = precision_recall_curve(self.__y_test, self.__y_pred)
        f1s = (2 * precision[:-1] * recall[:-1]) / (precision[:-1] + recall[:-1])
        best_th = np.argmax(f1s)
        plt1.plot(th[best_th], f1s[best_th], c='r', marker='o')
        plt1.plot([th[best_th], th[best_th]], [0.0,f1s[best_th] ], 'r--')
        plt1.plot([0.0, th[best_th]], [f1s[best_th], f1s[best_th] ], 'r--')
        plt1.annotate('Pre: %0.3f, Rec: %0.3f' %(precision[best_th], recall[best_th]), 
                    xy=(th[best_th]+ 0.01, f1s[best_th]-0.05))
        plt1.grid(True)

        plt2 = figure.add_subplot(122)
        plt2.hist(preds_with_true_labels[preds_with_true_labels[:, 1] == 0][:, 0], 
                label=name_positive, color='royalblue', alpha=1)
        plt2.hist(preds_with_true_labels[preds_with_true_labels[:, 1] == 1][:, 0], 
                label=name_negative, color='darkcyan', alpha=0.8)
        plt2.set_ylabel('Number of examples')
        plt2.set_xlabel('Probabilities')
        plt2.set_title('Probability histogram')
        plt2.legend(bbox_to_anchor=(1, 1))

        plt.show()

    def __show_probabilities_threshold_calibration(self, ax:Axes):
        thresholds = []
        precisions = []
        recalls = []
        f1_scores = []

        for threshold in np.linspace(0.1, 0.9, 100):
            thresholds.append(threshold)
            precisions.append(precision_score(self.__y_test, list(map(int, self.__y_pred > threshold))))
            recalls.append(recall_score(self.__y_test, list(map(int, self.__y_pred > threshold))))
            f1_scores.append(f1_score(self.__y_test, list(map(int, self.__y_pred > threshold))))

        scores_table = pd.DataFrame({'f1':f1_scores,
                                    'precision':precisions,
                                    'recall':recalls,
                                    'probability':thresholds}).sort_values('f1', ascending=False).round(3)

        ax.plot(thresholds, precisions, label='Precision', linewidth=2)
        ax.plot(thresholds, recalls, label='Recall', linewidth=2)
        ax.plot(thresholds, f1_scores, label='F1', linewidth=2)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Probability threshold')
        ax.set_title('Probabilities threshold calibration')
        ax.legend(bbox_to_anchor=(0.25, 0.25))  

        self.__metric.Precision
        precision = self.__metric.Precision
        recall = self.__metric.Recall
        th = self.__metric.Thresholds
        #precision, recall, th = precision_recall_curve(self.__y_test, self.__y_pred)
        #f1s = (2 * precision[:-1] * recall[:-1]) / (precision[:-1] + recall[:-1])
        # best_th = np.argmax(f1s)
        # ax.plot(th[best_th], f1s[best_th], c='r', marker='o')
        # ax.plot([th[best_th], th[best_th]], [0.0,f1s[best_th] ], 'r--')
        # ax.plot([0.0, th[best_th]], [f1s[best_th], f1s[best_th] ], 'r--')
        # ax.annotate('Pre: %0.3f, Rec: %0.3f' %(precision[best_th], recall[best_th]), 
        #             xy=(th[best_th]+ 0.01, f1s[best_th]-0.05))
        f1s = self.__metric.Fscore
        ax.plot(th, f1s, c='r', marker='o')
        ax.plot([th, th], [0.0,f1s ], 'r--')
        ax.plot([0.0, th], [f1s, f1s ], 'r--')
        ax.annotate('Pre: %0.3f, Rec: %0.3f' %(precision, recall), 
                    xy=(th+ 0.01, f1s-0.05))
        ax.grid(True)

    def __show_probability_histogram(self, 
        ax:Axes,
        name_negative:str = 'Main class', # 0
        name_positive:str = 'Another class', # 1
    ):
        ax.hist(self.__y_pred[~self.__y_test.astype(bool)], bins=100, alpha=0.7, label=name_negative)
        ax.hist(self.__y_pred[self.__y_test.astype(bool)], bins=100, alpha=0.7, label=name_positive)

        ax.set_ylabel('Number of examples')
        ax.set_xlabel('Probabilities')
        ax.set_title('Probability histogram')
        ax.legend(bbox_to_anchor=(1, 1))

    def __show_test_value_counts(self, 
        ax:Axes,
        name_negative:str = 'Main class', # 0
        name_positive:str = 'Another class', # 1
    ):
        # ax = self.__y_test.value_counts().plot.pie(autopct="%.2f")
        # _ = ax.set_title("Распределение y_test")
        ax.set_title("Pie chart: test value")
        ax.pie(self.__y_test.value_counts(), labels=[name_negative, name_positive], autopct='%1.1f%%',shadow=True, startangle=45)
        #ax.axis('equal')

    def __show_confusion_matrix(self,
        ax:Axes,
        name_negative:str = '0', 
        name_positive:str = '1', 
    ):
        self.__metric.Confusion_matrix.show_table(ax, name_positive=name_positive, name_negative=name_negative)

    def __show_roc_auc(self,
        ax:Axes
    ):
        fpr, tpr, roc_thresholds = roc_curve(self.__y_test, self.__y_pred)
        ax.plot(fpr, tpr, label='%s: ROC curve (area = %0.2f)' % (self.__name, auc(fpr, tpr)), color='r')
        ax.plot([0, 1], [0, 1], 'k--')
        ax.axis([0.0, 1.0, 0.0, 1.05])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('%s: Receiver operating characteristic curve' % self.__name)
        ax.legend(loc="lower right")

    def __show_precision_recall_curve(self,
        ax:Axes
    ):
        precision, recall, pr_thresholds = precision_recall_curve(self.__y_test, self.__y_pred)
        ax.plot(recall, precision, label='%s: Precision-Recall curve (area = %0.2f)' % (self.__name, auc(recall, precision)), color='r')
        ax.set_xlabel('Recall')
        ax.set_ylabel('Precision')
        ax.set_title("%s: Precision-Recall curve" % self.__name)
        ax.axis([0.0, 1.0, 0.0, 1.05])
        ax.legend(loc="lower left")

    def show_chart_report(self,
        name_negative:str = 'Main class', # 0
        name_positive:str = 'Another class', # 1
    ):
        fig, ((ax11, ax12, ax13), (ax21, ax22, ax23)) = plt.subplots(2, 3, figsize=(20,10))
        fig.suptitle(f'Charts: {self.Name}', fontsize=16)
        self.__show_probabilities_threshold_calibration(ax11)
        self.__show_probability_histogram(ax12, name_negative, name_positive)
        self.__show_test_value_counts(ax13, name_negative, name_positive)
        self.__show_confusion_matrix(ax21, name_negative, name_positive)
        self.__show_roc_auc(ax22)
        self.__show_precision_recall_curve(ax23)
        fig.tight_layout()
        plt.show()
    
    def add_roc_chart(self, ax:Axes):
        fpr, tpr, roc_thresholds = roc_curve(self.__y_test, self.__y_pred)
        ax.plot(fpr, tpr, label=f'{self.__name}: ROC (AUC = {auc(fpr, tpr):.2f})', lw=2, alpha=.8)
    
    def add_pr_chart(self, ax:Axes):
        precision, recall, pr_thresholds = precision_recall_curve(self.__y_test, self.__y_pred)
        ax.plot(recall, precision, label=f'{self.__name}: PR (AUC = {auc(recall, precision):.2f})', lw=2, alpha=.8)

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
        return self.__repo[name].calc_metric()

    def __short_format(self, value: float):
        return '%.3f' % (value)

    def show_table_report(self):   
        self.__calc_metrics()
        self.__show_table_report()

    def __show_table_report(self):
        table = list()
        experiment:Experiment = None
        for name, experiment in self.__repo:
            table.append([
                name,
                self.__short_format(experiment.metric.Thresholds),
                self.__short_format(experiment.metric.Fscore),
                self.__short_format(experiment.metric.Precision),
                self.__short_format(experiment.metric.Recall),               
                self.__short_format(experiment.metric.Roc_AUC)              
            ])
        print(tabulate(table, headers=['Name model','Threshold', 'F-Score', 'Precision', 'Recall', 'Roc-AUC']))

    def get_experiment(self, name:str)->Experiment:
        return self.__repo[name]

    def show_full_report(self,
        name_negative:str = 'Main class', # 0
        name_positive:str = 'Another class', # 1
    ):
        metrics = self.__calc_metrics()
        self.__show_charts_report(name_negative, name_positive)
        self.__show_table_report()

    def __show_charts_report(self,
        name_negative:str = 'Main class', # 0
        name_positive:str = 'Another class', # 1
    ):
        experiment:Experiment = None
        for name, experiment in self.__repo:
            experiment.show_chart_report(name_negative, name_positive)

    def __calc_metrics(self)->Dict[str, Metric]:
        metrics: Dict[str, Metric] = dict()
        name :str = None
        experiment:Experiment = None
        for name, experiment in self.__repo:
            metrics[name] = experiment.calc_metric() 
        return metrics

    def show_united_auc(self):
        fig, ((ax1, ax2)) = plt.subplots(1, 2,figsize=(12,5))
        fig.suptitle('AUC', fontsize=16)
        ax1.plot([0, 1], [0, 1], linestyle='--', lw=2, label='Chance', alpha=.8)
        experiment:Experiment = None
        for name, experiment in self.__repo:
            experiment.add_roc_chart(ax1)
            experiment.add_pr_chart(ax2)
        ax1.legend(loc="lower right")
        ax2.legend(loc="lower right")
        fig.tight_layout()
        plt.show()
