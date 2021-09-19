from random import choice, sample


class Card(object):
    def __init__(self):
        pos_gen = CardPositionGenerator()
        self.__repo = list()
        for _ in range(3):
            row = list()
            for item in sorted([pos_gen.get_random_position() for _ in range(5)]):
                row.append(item)    
            self.__repo.append(row)
        self.__repo_display = list()
        for row_num in range(3):
            empty_position = sorted(sample(range(9), 4))
            row = list(self.__repo[row_num])
            for item in empty_position:
                row.insert(item, ' ')
            self.__repo_display.append(row)      

    def __str__(self):
        result = ''
        for row_num in range(3):
            for column_num in range(9):
                result = result+ f'{self.__repo_display[row_num][column_num]:4}'
            result = result + '\n'
        return result

    def cross_piece(self, piece):
        for row in range(3):
            for column in range(5):
                if self.__repo[row][column].cross(piece):
                    return True
        return False

    def contained_piece(self, piece):
        for row in range(3):
            for column in range(5):
                if self.__repo[row][column].number == piece.number:
                    return True
        return False

    def is_all_cross(self):
        for row in range(3):
            for column in range(5):
                if not self.__repo[row][column].is_cross:
                    return False
        return True

class CardPosition(object):
    def __init__(self, number):
        self.__number = number
        self.__is_cross =False
        
    @property
    def number(self):
        return self.__number

    @property
    def is_cross(self):
        return self.__is_cross

    def __lt__(self,other):
        return self.__number < other.number

    def __gt__(self,other):
        return self.__number > other.number

    def __str__(self):
        return str(self.__number)

    def __format__(self, fmt):
        if self.is_cross:
            symbol = '--'
            return f'{symbol:>{fmt}}'    
        return f'{self.__number:{fmt}}'

    def cross(self, piece):
        if self.number == piece.number:
            self.__is_cross =True
            return True
        return False


class CardPositionGenerator(object):
    def __init__(self):
        self.__number_list = [number for number in range(1, 91)]

    def get_random_position(self):
        if len(self.__number_list)==0:
            return None
        number = choice(self.__number_list)
        self.__number_list.remove(number)
        return CardPosition(number)