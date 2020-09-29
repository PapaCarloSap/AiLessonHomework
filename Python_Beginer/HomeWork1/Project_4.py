user_value = int(input('Enter number: '))
max_value = user_value % 10
buffer = user_value // 10
while not(buffer == 0 or max_value == 9):
    next_num = buffer % 10
    if max_value<next_num:
        max_value = next_num
    buffer = buffer // 10
    
print(f'Max value: {max_value}')