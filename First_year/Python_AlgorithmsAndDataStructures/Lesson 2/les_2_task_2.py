    """
    Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, 
    в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
    """

user_data = input('Input numbers: ')
even_list = list()
odd_list = list()
for i in range(len(user_data)):
    item = int(user_data[i])
    if((item&1)==1):
        odd_list.append(item)
    else:
        even_list.append(item)

print('the number of odd: {0} {1}'.format(len(odd_list), odd_list))
print('the number of even: {0} {1}'.format(len(even_list), even_list))