from modules.matrix import Matrix


def scan_matrix():
    matrix_kol = int(input())
    arr = []
    for i in range(matrix_kol):
        cur_kol = int(input())
        cur_sum = 0
        for j in range(cur_kol):
            cur_str = list(map(int, input().split()))
            cur_sum += cur_str[j]
        arr.append(Matrix(i, cur_sum))
    return arr
