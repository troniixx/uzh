class Matrix:

    def __init__(self, matrix):
        assert matrix != [], 'empty list'
        assert isinstance(matrix, list), 'not a nested list'
        for row in matrix:
            assert isinstance(row, list), 'not a nested list'
            assert row != [], 'empty sublist'
            assert len(row) == len(matrix[0]), 'matrix not rectangular'
            for num in row:
                assert isinstance(num, (int, float)), 'invalid type in sublist'
        self.__matrix = matrix

    def __add__(self, other):
        
        # validate operation
        assert isinstance(other, Matrix), 'not a matrix'
        rows = len(self.__matrix)
        cols = len(self.__matrix[0])
        assert rows == len(other.__matrix), 'not the same number of rows'
        assert cols == len(other.__matrix[0]), 'not the same number of columns'

        # create matrix with correct size
        sum = []
        for i in range(rows):
            sum.append([])
            for j in range(cols):
                sum[i].append(0)

        # fill in sums
        for i in range(rows):
            for j in range(cols):
                sum[i][j] = self.__matrix[i][j] + other.__matrix[i][j]

        return Matrix(sum)

    def __mul__(self, other):

        # validate operation
        assert isinstance(other, Matrix), 'not a matrix'
        rows1 = len(self.__matrix)
        cols1 = len(self.__matrix[0])
        rows2 = len(other.__matrix)
        cols2 = len(other.__matrix[0])
        assert cols1 == rows2, 'number of colums (1st matrix) != number of rows (2nd matrix)'
        
        # create matrix with correct size
        prod = []
        for i in range(rows1):
            prod.append([])
            for j in range(cols2):
                prod[i].append(0)

        # fill in prods
        for i in range(rows1):
            for j in range(cols2):
                for k in range(rows2):
                    prod[i][j] += self.__matrix[i][k] * other.__matrix[k][j]

        return Matrix(prod)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.__matrix]))

    def __repr__(self):
        return repr(self.__matrix)


if __name__ == '__main__':
    M = Matrix([[5,5],[5,5]])
    T = Matrix([[5,5],[5,5]])
    print(M)
    print(M == T)
    d = {M: "1", T: "2"}
    d.update({M: "3"})
    print(d)