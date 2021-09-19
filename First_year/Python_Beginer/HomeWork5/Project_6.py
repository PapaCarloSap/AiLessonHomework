import Helper

file_path = '.\\HomeWork5\\Project_6.temp'
Helper.check_exist_file(file_path)

dic={}
with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        name, lection, practic, lab = line.split()
        total = sum([int(lection[0:-3]) if lection != '—' else 0, int(practic[0:-4]) if practic != '—' else 0, int(lab[0:-5]) if lab != '—' else 0])
        dic.update([(name[0:-1], total)])
print(dic)