    """
    Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
    """
#%%
bit_or = 5 | 6
bit_and = 5 & 6
bit_xor = 5 ^ 6
bit_shift = (5>>2)<<2

print(f'5 | 6 = {bit_or}')
print(f'5 & 6 = {bit_and}')
print(f'5 ^ 6 = {bit_xor}')
print(f'(5>>2)<<2 = {bit_shift}')