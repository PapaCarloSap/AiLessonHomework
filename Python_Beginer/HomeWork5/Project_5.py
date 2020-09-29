import random


with open('.\\HomeWork5\\project_5.temp', 'w') as f:
    for _ in range(random.randint(5, 20)):
        f.write(f'{random.uniform(0, 100):.3f} ')

with open('.\\HomeWork5\\project_5.temp', 'r') as f:
    print(f'Сумма чисел: {sum([float(item) for item in f.readline().split()]):.3f}')