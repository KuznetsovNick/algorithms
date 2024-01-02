from modules.hash import func_hash


def solve(pattern, text):
    answer = []
    p = 1000000007
    x = 263

    len_pattern = len(pattern)
    len_text = len(text)
    hash_arr = [0] * (len_text - len_pattern + 1)
    degree = [1] * (len_pattern + 1)
    for i in range(len_pattern):
        degree[i+1] = (degree[i] * x) % p
    hash_arr[-1] = func_hash(text[len_text - len_pattern:], p, degree)
    for i in range(len_text - len_pattern - 1, -1, -1):
        hash_arr[i] = (ord(text[i]) + (x * hash_arr[i+1]) % p - (ord(text[i+len_pattern]) * degree[len_pattern-1]) * x % p) % p
    hash_pattern = func_hash(pattern, p, degree)
    for i, element in enumerate(hash_arr):
        if element == hash_pattern and pattern == text[i: i+len_pattern]:
            answer.append(i)
    return answer
