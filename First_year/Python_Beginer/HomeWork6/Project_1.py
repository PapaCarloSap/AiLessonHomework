import time

class TrafficLight:
    __color = ''

    def running(self):
        __color = 'Красный'  
        yield __color
        time.sleep(7)
        __color = 'Желтый'  
        yield __color
        time.sleep(2)
        __color = 'Зеленый'  
        yield __color
        time.sleep(5)

def custome_print(data):
    print(data)
    return data

traffic_light = TrafficLight()
result = list(map(lambda item: custome_print(item), traffic_light.running()))
check = len(result)==3 and len([(i,j) for i, j in zip(result, ['Красный', 'Желтый', 'Зеленый']) if i!=j ])==0
print_result = ('верный', 'не верный')
print(f'Результат \'{print_result[0] if check else print_result[1]}\'')

