class Car:
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Turn: \'{direction}\'')

    def show_speed(self):
        print(f'Current speed: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print(f'High speed: {self.speed}')
        else:
            super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed>40:
            print(f'High speed: {self.speed}')
        else:
            super().show_speed()

class PoliceCar(Car):
    pass

def show_result(any_car):
    print(f'Speed: {any_car.speed}')
    print(f'Color: {any_car.color}')
    print(f'Name: {any_car.name}')
    print(f'Является ли полицейчкой: {any_car.is_police}')
    any_car.go()
    any_car.turn('left')
    any_car.turn('right')
    any_car.show_speed()
    any_car.stop()
    print('------------------------------')

car = Car(10,'red', 'car', False)
show_result(car)

car = TownCar(70,'blue', 'TownCar', False)
show_result(car)

car = TownCar(50,'blue', 'TownCar', False)
show_result(car)

car = SportCar(100,'white', 'SportCar', False)
show_result(car)

car = WorkCar(80,'green', 'WorkCar', False)
show_result(car)

car = WorkCar(30,'green', 'WorkCar', False)
show_result(car)

car = PoliceCar(50,'green', 'PoliceCar', True)
show_result(car)