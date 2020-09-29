import Helper

file_path = '.\\HomeWork5\\project_3.temp'
Helper.check_exist_file(file_path)

# read file
repo = {}
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        key, value = line.strip().split()
        repo.update([(key, value)])

# determine the answers
sum_salary = 0        
for key, value in repo.items():
    salary = float(value)
    if salary<20000:
        print(f'Меньше 20000 оклад имеет \'{key}\' с окладом \'{value}\'')
    sum_salary += salary
print(f'Средняя величина: {sum_salary/len(repo)}')