income = int(input('Введите выручку: '))
expenditure = int(input('Введите расход: '))
is_profit = False

if income > expenditure:
    profit = income - expenditure
    print(f'Фирма отработала с прибылью: {profit}р.')
    is_profit = True
elif income < expenditure:
    print(f'Фирма отработала с убытком: {income-expenditure}р.')
else:
    print(f'Фирма просто поработала')

if is_profit:
    print(f'Рентабельность {profit/income}')
    personal = int(input('Введите численность сотрудников: '))
    print(f'Прибыль на одного сотрудника: {profit/personal}')
