def get_user_info(
    name = '-', 
    surname = '-', 
    birth_year = '-', 
    city = '-', 
    email = '-', 
    phone = '-'):
    return f'Name: {name}, Surname {surname}, Birth year: {birth_year}, City {city}, Email {email}, Phone {phone}'

print(get_user_info(
    name='Alex',
    surname='Ivanov',
    city='Moscow',
    email='qqqq@qqq.qq'
))