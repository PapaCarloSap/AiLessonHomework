from abc import ABC, abstractmethod

class Clothe(ABC):
    @abstractmethod
    def get_consumption(self):
        pass

    def __add__(self, clothe):
        return Canvas(self.get_consumption()+clothe.get_consumption())

class Canvas(Clothe):

    def __init__(self, area):
        self.__area = area

    @property
    def area(self):
        return self.__area

    def get_consumption(self):
        return self.__area


class Coat(Clothe):
    
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def get_consumption(self):
        return self.__size/0.6 + 0.5


class Suit(Clothe):
    
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    def get_consumption(self):
        return 2*self.__height + 0.3


def main():
    
    coat1 = Coat(3)
    coat2 = Coat(1)
    suit = Suit(2)

    print(f'Coat 1: {coat1.size}')
    print(f'Coat 2: {coat2.size}')
    print(f'Suit: {suit.height}')

    canvas = coat1 + coat2 + suit

    print(f'Размер полотна: {canvas.area:.6}')


if __name__ == '__main__':
    main()   