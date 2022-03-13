from typing import List

class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        result = List.deepList(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                result[i][k] = self.matrix[i][k] + other.matrix[i][k]
                return Matrix(result)



if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    print(first_matrix, '\n')
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(second_matrix, '\n')


print('first_matrix + second_matrix')


