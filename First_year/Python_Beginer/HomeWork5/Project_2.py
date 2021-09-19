import Helper


file_path = '.\\HomeWork5\\project_2.temp'
Helper.check_exist_file(file_path)

with open(file_path) as f:
    number_of_line = 0
    for line in f:
        number_of_line += 1
        print(f'В cтроке \'{number_of_line}\' количество слов \'{len(line.split())}\'')

print(f'Всего количество строк: {number_of_line}')