var_sec = int(input('Введите значение в секугдах: '))
hh = int(var_sec/3600)
mm = int((var_sec-(hh*3600))/60)
ss = int(var_sec-(hh*3600+mm*60))

print(f'Это соответетсвует: {hh}:{mm}:{ss}')