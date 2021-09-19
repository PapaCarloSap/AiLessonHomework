with open('.\\HomeWork5\\project_1.temp', 'w') as f:
    while True:
        data = input('Введите текст: ')
        if data == ' ':
            f.close()
            exit(0)
        f.write(data + '\n')