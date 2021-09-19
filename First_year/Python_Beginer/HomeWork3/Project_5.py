def get_float_list(str_list):
    is_last_data = False
    float_list = []
    for item in str_list:
        if item == 'exit':
            is_last_data = True
            break
        float_list.append(float(item))
    
    return is_last_data, float_list

def get_user_data():
    while True:
        user_data = input("Введите числа ('exit' для выхода): ").split(' ')          
        try:
            return get_float_list(user_data)
        except :
            print('Числа введены не верно')
            continue
        
user_sum = 0
while True:
    is_last_data, float_list = get_user_data()
    user_sum = user_sum + sum(float_list)
    print(f'Сумма: {user_sum}')
    if is_last_data:
        exit(0)
        
