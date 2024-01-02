from modules.merge import merge
from modules.matrix import Matrix


def test1():
    matrix0 = Matrix(0, -245)
    matrix1 = Matrix(1, 228)
    matrix2 = Matrix(2, 147)
    matrix3 = Matrix(3, -99)
    matrix4 = Matrix(4, -113)
    matrix_list = [matrix0, matrix1, matrix2, matrix3, matrix4]
    matrix_result = [matrix0, matrix4, matrix3, matrix2, matrix1]
    assert merge(matrix_list) == matrix_result


def test2():
    matrix0 = Matrix(0, 69)
    matrix_list = [matrix0]
    matrix_result = [matrix0]
    assert merge(matrix_list) == matrix_result


def test3():
    matrix0 = Matrix(0, -87)
    matrix1 = Matrix(1, 93)
    matrix2 = Matrix(2, 111)
    matrix_list = [matrix0, matrix1, matrix2]
    matrix_result = [matrix0, matrix1, matrix2]
    assert merge(matrix_list) == matrix_result

