def get_max_sum(a, b, c):
    values = [a,b,c]
    min_value = min(values)
    values.remove(min_value)
    return sum(values)
    