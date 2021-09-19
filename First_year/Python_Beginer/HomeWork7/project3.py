from math import ceil

class Cell(object):
    
    def __init__(self, point):
        self._point = point

    def __add__(self, cell):
        return Cell(self._point + cell._point)
        
    def __sub__(self, cell):
        result = self._point - cell._point
        if result>0:
            return Cell(self._point - cell._point)
        else:
            return 'Не возможно выполнить вычитание ячеек из клетки'

    def __mul__(self, cell):
        return Cell(self._point * cell._point)

    def __truediv__(self, cell):
        return Cell(ceil(self._point / cell._point))

    def make_order(self, size_line):
        return ('*'*size_line+'\n')*(self._point//size_line) + '*'*(self._point%size_line)

    def __str__(self):
        return f'Cell.point = {self._point}'

def main():
    cell1 = Cell(5)
    cell2 = Cell(4)
    print(cell1+cell2)
    print(cell1-cell2)
    print(cell1*cell2)
    print(cell1/cell2)
    print('-'*10+'Cell 1'+'-'*10)
    print(cell1.make_order(2))
    print('-'*10+'Cell 2'+'-'*10)
    print(cell2.make_order(3))

if __name__ == '__main__':
    main()   