from tokenize import Name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from sklearn import metrics
from sklearn.metrics import f1_score, roc_auc_score, precision_score, precision_recall_curve, confusion_matrix, recall_score
from tabulate import tabulate
from deprecated import deprecated


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
        name_positive:str = 'Positive', 
        name_negative:str = 'Negative', 
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
        name_positive:str = 'Another class', 
        name_negative:str = 'Main class', 
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

    def calc_metrics(self):   
        table = list()
        for name, experiment in self.__repo:
            metric = experiment.calc_metric()
            table.append([
                name,
                self.__short_format(metric.Thresholds),
                self.__short_format(metric.Fscore),
                self.__short_format(metric.Precision),
                self.__short_format(metric.Recall),               
                self.__short_format(metric.Roc_AUC)              
            ])
        print(tabulate(table, headers=['Name model','Threshold', 'F-Score', 'Precision', 'Recall', 'Roc-AUC', 'Profit $']))

    def get_experiment(self, name:str)->Experiment:
        return self.__repo[name]

