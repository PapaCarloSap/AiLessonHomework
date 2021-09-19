def get_exponentiation(x, y):
    if y<0:
        return 1/get_exponentiation(x, int(y/-1))   
    else:
        buffer = 1
        for _ in range(y):
            buffer = buffer*x
        return float(buffer)