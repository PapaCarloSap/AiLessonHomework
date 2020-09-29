'''
Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
'''
import random

source_list = [random.randint(0, 99) for _ in range(random.randint(10,21))]
print(source_list)
result_list = list()
for i, item in enumerate(source_list):
    if (item&1)==0:
        result_list.append(i)

print(result_list)