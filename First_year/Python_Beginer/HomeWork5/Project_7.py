import Helper
import json

file_path = '.\\HomeWork5\\Project_7.temp'
Helper.check_exist_file(file_path)

repo = {}
total_profit = 0
total_firm_profit = 0
# with open(file_path, 'r', encoding='utf-8') as f:
#     repo_list = [name, firm_type, float(revenue), float(expenses) for name, firm_type, revenue, expenses in f.readline().split()]
with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        name, firm_type, revenue, expenses = line.split() 
        repo.update([(name, [firm_type, float(revenue), float(expenses)])])
        print(f'Для: {name} прибыль: {repo[name][1]-repo[name][2]}')
        if repo[name][1]>=repo[name][2]:
            total_firm_profit +=1
            total_profit += repo[name][1]-repo[name][2]
average_profit=total_profit/total_firm_profit
print(f'Средняя прибыль: {average_profit}')            

dic_profit={}
for name, data in repo.items():
    dic_profit.update([(name, data[1]-data[2])])
dic_result = [dic_profit, {'average_profit': average_profit}]
with open('.\\HomeWork5\\Project_7.json', 'w') as f_json:
    json.dump(dic_result, f_json)

