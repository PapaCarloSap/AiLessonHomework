import random


class Piece(object):
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return str(self.__number)


class Pieces(object):
    def __init__(self):
        self.__piece_list = [Piece(number) for number in range(1, 91)]

    def get_random_piece(self):
        if len(self.__piece_list)==0:
            return None
        piece = random.choice(self.__piece_list)
        self.__piece_list.remove(piece)
        return piece

    @property
    def count(self):
        return len(self.__piece_list)

    def is_empty(self):
        return len(self.__piece_list) == 0
