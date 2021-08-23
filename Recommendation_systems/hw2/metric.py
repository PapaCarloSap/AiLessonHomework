import numpy as np
import math 
from typing import Dict, Iterator, List, NoReturn
from deprecated import deprecated
from tabulate import tabulate

class Experiment:
    def __init__(self, recommended:np.array, boughted:np.array, name:str):
        """Experiment for analysis

        Args:
            recommended (np.array): Any product recommended for the user
            boughted (np.array): Any product purchased by the user
        """
        self.__recommended = recommended
        self.__boughted = boughted
        self.__name = name

    def hit_rate(self)->bool:
        """ Был ли хотя бы 1 релевантный товар среди рекомендованных
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#1-hit-rate
        Returns:
            bool: True - there is one or more, False - nothing
        """
        flags = np.isin(self.__boughted, self.__recommended)
        hit_rate = flags.sum() > 0
        return hit_rate

    def hit_rate_at_k(self, k:int=5)->bool:
        """Был ли хотя бы 1 релевантный товар среди k рекомендованных
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#1-hit-rate
        Args:
            k (int, optional): The number of recommended. Defaults to 5.

        Returns:
            bool: True - there is one or more, False - nothing
        """
        flags = np.isin(self.__boughted, self.__recommended[:k])
        hit_rate = flags.sum() > 0
        return hit_rate
    
    def precision(self)->float:     
        """ доля купленых товаров из рекомендованых товаров
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#2-precision

        Returns:
            float: доля купленных товаров (0..1)
        """
        flags = np.isin(self.__boughted, self.__recommended)
        precision = flags.sum() / len(self.__recommended)
        return precision

    def precision_at_k(self, k=5)->float:
        """доля купленых товаров для k рекомендованых товаров
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#2-precision


        Args:
            k (int, optional): The number of recommended. Defaults to 5. Ususaly 5-20

        Returns:
            float: доля купленных товаров (0..1)
        """
        recommended_list = self.__recommended[:k]
        flags = np.isin(self.__boughted, recommended_list)
        precision = flags.sum() / len(recommended_list)
        return precision

    @deprecated(reason='для prices_recommended возможно лучше взять Dict[int, float]. Посмотрим по опыту использования')
    def money_precision_at_k(self, prices_recommended:List[float], k:int=5)->float:   
        """доля потраченных денег на купленые товары для k рекомендованых товаров
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#2-precision

        Args:
            prices_recommended (List[float]): Стоимость товара int - id товара, float - цена
            k (int, optional): The number of recommended. Defaults to 5.

        Returns:
            float: доля  потраченных денег (0..1)
        """
        bought_list = self.__boughted  # Тут нет [:k] !!
        recommended = self.__recommended[:k]
        flags = np.isin(bought_list, recommended)
        precision = np.sum(
            np.take(                            # потрачено денег на товары из рекомендованного списка
                prices_recommended, 
                [bought_list[idx] for idx, val in enumerate(flags) if val]
                )
            ) / np.sum(prices_recommended)      # Рекомендованно товаров на сумму
        return precision

    def recall(self)->float:
        """доля рекомендованых товаров для купленных товаров
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#3-recall

        Returns:
            float: [description]
        """
        flags = np.isin(self.__boughted, self.__recommended)
        recall = flags.sum() / len(self.__boughted)
        return recall

    def recall_at_k(self, k:int=50)->float:
        """доля k рекомендованых товаров для купленных товаров
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#3-recall

        Args:
            k (int, optional): The number of recommended. Defaults to 50. Ususaly 50-200

        Returns:
            float: доля рекомендованых товаров (0..1)
        """
        flags = np.isin(self.__boughted, self.__recommended[:k])
        recall = flags.sum() / len(self.__boughted)
        return recall
    
    def money_recall_at_k(self, prices:Dict[int, float], k:int=5)->float:   
        """доля потраченных денег на купленые товары для k рекомендованых товаров
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#3-recall

        Args:
            prices_recommended (List[float]): Стоимость товара int - id товара, float - цена
            k (int, optional): The number of recommended. Defaults to 5.

        Returns:
            float: доля потраченных денег (0..1)
        """
        bought_list = self.__boughted  # Тут нет [:k] !!
        recommended = self.__recommended[:k]
        flags = np.isin(bought_list, recommended)
        precision = np.sum(
            sum([prices[key] for key in [bought_list[idx] for idx, val in enumerate(flags) if val]]) # потраченных денег на товар из рекомендованного списка 
            ) / np.sum([prices[idx] for idx in bought_list]) # всего потраченных денег на товары
        return precision

    def ap_k(self, k:int=5)->float:
        """average precision at k

        Args:
            k (int, optional): Кол-во рекомендованных. Defaults to 5.

        Returns:
            float: оценка
        """
        flags = np.isin(self.__recommended, self.__boughted)
        if sum(flags) == 0:
            return 0
        precisions = sum([self.precision_at_k(k=idx) for idx in range(1, k+1) if flags[idx-1] ])
        result = precisions / len(flags)
        return result

    def dcg_k(self, k:int=5, ideal:bool=False)->float:
        """discounted cumulative gain
            http://kb.local:8090/pages/viewpage.action?pageId=36438375#ndcg-k

        Args:
            k (int, optional): Для первых k рекоммендаций. Defaults to 5.
            ideal (bool, optional): Идеальный DCG@k. Defaults to False.

        Returns:
            [type]: оценка 0..1
        """
        dcg_log = lambda x : 1 if x==1 else math.log(x)
        if ideal:
            sum_log = sum([dcg_log(idx+1) for idx in range(0, k)]) 
        else:
            flags = np.isin(self.__recommended[:k], self.__boughted)
            sum_log = sum([dcg_log(idx+1) for idx in range(0, k) if flags[idx]]) 
        return 1/k * sum_log

    def ndcg_k(self, k:int=5):
        """Normalized discounted cumulative gain
        http://kb.local:8090/pages/viewpage.action?pageId=36438375#ndcg-k

        Args:
            k (int, optional): для первых k рекоммендаций. Defaults to 5.

        Returns:
            [type]: оценка 0..1
        """
        return  self.dcg_k(k)/self.dcg_k(k, ideal=True)

    def mrr(self, k:int=None)->float:
        """Mean Reciprocal Rank
        изменяется в диапазоне [0,1] и учитывает позицию элементов. 
        К сожалению он делает это только для одного элемента — 1-го верно предсказанного, не обращая внимания на все последующие.

        Args:
            k (int, optional): для первых k рекоммендаций. Defaults to None. None - для всех рекоммендаций

        Returns:
            [type]: оценка 0..1
        """
        ranks=0.
        recommended = self.__recommended if k is None else self.__recommended[:k]
        for i, item_rec in enumerate(recommended):
            for item_bought in self.__boughted:
                if item_rec == item_bought:
                    ranks += 1 / (i+1)
        return ranks / len(recommended)


class ExperimentRepository:
    
    __repo : Dict[str, List[Experiment]] = dict()

    def __init__(self) -> None:
        pass

    def __iter__(self) -> Iterator[List[Experiment]]:
        return iter(self.__repo.items())

    def __next__(self) -> List[Experiment]:
        return next(iter(self.__repo.items()))
        return next(self.__repo)

    def __len__(self) -> int:
        return len(self.__repo)

    def __getitem__(self, key:str) -> List[Experiment]:
        return self.__repo.get(key)

    def append(self, name:str, experement: Experiment):
        lst = self.__repo.get(name)
        if lst is None:
            self.__repo.update({name:[experement]})
        else:
            lst.append(experement)
            
    
    def show_table(self)->NoReturn:
        pass


class MetricManager:
    __repo : ExperimentRepository = ExperimentRepository()

    # def __init__(self):
    #     self.__repo = ExperimentRepository() 
        #self.__business_case = BusinessCase(fine_good = fine_good, fine_toxic=fine_toxic)

    def apply(self, name:str, recommended: np.array, boughted: np.array, user:str):
        self.__repo.append(name, Experiment(recommended, boughted, user))

    def __short_format(self, value: float):
        return '%.3f' % (value)

    def show_table(self):   
        table = list()
        for name, experiments in self.__repo:           
            table.append([
                name,
                self.__short_format(np.array([experiment.hit_rate_at_k() for experiment in experiments]).mean()),
                self.__short_format(np.array([experiment.precision_at_k() for experiment in experiments]).mean()),
                #self.__short_format(np.array([experiment.recall_at_k() for experiment in experiments]).mean()),
                self.__short_format(np.array([experiment.ap_k() for experiment in experiments]).mean()),               
                self.__short_format(np.array([experiment.dcg_k() for experiment in experiments]).mean()), 
                self.__short_format(np.array([experiment.ndcg_k() for experiment in experiments]).mean()), 
                self.__short_format(np.array([experiment.mrr() for experiment in experiments]).mean()),              
            ])
        print(tabulate(table, headers=[
            'Name model',
            'Hit rate', 
            'Precision', 
            #'Recall', 
            'Average precision', 
            'DCG', 
            'NDCG',
            'MRR']))

    def get_experiment(self, name:str)->Experiment:
        return self.__repo[name]