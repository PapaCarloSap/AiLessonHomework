    """
    Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
    Количество элементов (n) вводится с клавиатуры.
    """

user_data = int(input('Input numbers: '))
i=1
num = 1
result = 0
while i<=user_data:
    result += num 
    num = (-1)*num/2
    i+=1
print(f'Result: {result}')