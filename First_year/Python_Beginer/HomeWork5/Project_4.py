import Helper

file_path_source = '.\\HomeWork5\\Project_4_source.temp'
file_path_result = '.\\HomeWork5\\Project_4_result.temp'
Helper.check_exist_file(file_path_source)

dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open(file_path_source, 'r', encoding='utf-8') as f_source:
    with open(file_path_result, 'w', encoding='utf-8') as f_result:
        for line in f_source:
            num, val = line.split(' — ')
            f_result.write(f'{dic[num]} — {val}')