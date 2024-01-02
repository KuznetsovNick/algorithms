from modules.matrix import Matrix


def merge(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    merge(left)
    merge(right)
    index_left = index_right = index = 0
    result = [Matrix(0, 0)] * (len(left) + len(right))
    while index_left < len(left) and index_right < len(right):
        if left[index_left].data <= right[index_right].data:
            result[index] = left[index_left]
            index_left += 1
        else:
            result[index] = right[index_right]
            index_right += 1
        index += 1
    while index_left < len(left):
        result[index] = left[index_left]
        index_left += 1
        index += 1
    while index_right < len(right):
        result[index] = right[index_right]
        index_right += 1
        index += 1

    output = []
    for i in range(len(arr)):
        arr[i] = result[i]
        output.append(str(result[i].ind))
    print(' '.join(output))
    return arr
