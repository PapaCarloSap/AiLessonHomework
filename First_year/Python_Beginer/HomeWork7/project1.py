class Matrix(object):
    def __init__(self, source):
        if len(source) == 0 or len(source[0]) == 0:
            raise ValueError(f'Invalid source: {source} ')
        self._source = source

    def _get_row_column(self, matrix):
        row = max(len(self._source), len(matrix._source))
        column = max(len(self._source[0]), len(matrix._source[0]))
        return [row, column]

    @staticmethod
    def _get_value_matrix(matrix, row, column):
        if len(matrix._source) > row and len(matrix._source[row]) > column:
            return matrix._source[row][column]
        else:
            return 0

    def __add__(self, matrix):
        row, column = self._get_row_column(matrix)
        result = [[0] * column for _ in range(row)]
        for i in range(row):
            for j in range(column):
                result[i][j] = self._get_value_matrix(self, i, j) + self._get_value_matrix(matrix, i, j)
        return Matrix(result)

    def __str__(self):
        result = ""
        for i in range(len(self._source)):
            for j in range(len(self._source[i])):
                result = f'{result}{self._source[i][j]}\t'
            result = f'{result}\n'
        return result


def main():
    matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
    matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
    matrix3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

    print(matrix1 + matrix2 + matrix3)


if __name__ == '__main__':
    main()
