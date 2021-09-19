def custom_div(data, divider):
    return data/divider

def convert_to_float(str):
    try:
        return float(str)
    except ValueError:
        return None

def convert_to_divisible_and_divider(a, b):
    divisible = convert_to_float(a)
    divider = convert_to_float(b)
    if divisible == None or divider==None :
        print('Числа введены не верно')
        return divisible, divider
    if divider == 0:
        print('Делитель не может быть равен 0')
        return divisible, None
    else:
        return divisible, divider

def get_user_value():
    while True:
        try:
            a, b = input("Введите делимое и делитель через пробел: ").split(' ')          
        except :
            print('Числа введены не верно')
            continue
        divisible, divider = convert_to_divisible_and_divider(a, b)
        if not divisible or not divider:
            continue
        else: 
            return divisible, divider

divisible, divider = get_user_value()   
print(f"Результат: {custom_div(divisible, divider)}")