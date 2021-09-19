values = [3, 3.14, True, 'Text']
for item in values:
    result = str(type(item)).split('\'')[1]
    print(f'{str(item):<10}{"--->":<10}{result}')

