while True:
    user_input = input('Введите номер месяца: ')
    try:
        user_month = int(user_input)
        if(user_month<=0 or user_month>12):
            print(f'Номер месяца \'{user_month}\' должно быть в пределах от 1 до 12')
            continue
        break
    except :
        print(f'Номер месяца \'{user_input}\' введене не верно')
month_list = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
season_dic = {'Декабрь': 'Зима', 'Январь': 'Зима','Февраль': 'Зима','Март': 'Весна','Апрель': 'Весна','Май': 'Весна','Июнь': 'Лето','Июль': 'Лето','Август': 'Лето','Сентябрь': 'Осень','Октябрь': 'Осень','Ноябрь': 'Осень'}
select_month = month_list[user_month-1]
print(f'Выбраный месяц: {select_month:<10} Пора года: {season_dic[select_month]}')