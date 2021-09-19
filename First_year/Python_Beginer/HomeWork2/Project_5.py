rating_list = [7,5,3,3,2]
while True:
    user_data = input('Введите любое натуральное число(для выхода введите \'ex\'):')
    if(user_data == 'ex'):
        exit(0)
    try:
        user_value = int(user_data)
    except :
        print(f'Введеное значение \'{user_data}\' не является целым числом')
        continue
    if(user_value<0):
        print(f'Введеное значение \'{user_data}\' не является натуральным числом')
        continue
    for index in range(len(rating_list)):
        if(user_value > rating_list[index]):
            rating_list.insert(index, user_value)
            print(f'Рейтинг: {rating_list}')
            break
    else:
        rating_list.append(user_value)
        print(f'Рейтинг: {rating_list}')
