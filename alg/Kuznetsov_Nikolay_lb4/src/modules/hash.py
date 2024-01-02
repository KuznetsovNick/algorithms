def func_hash(str, p, degree):
    result = 0 
    for i, element in enumerate(str):
        result = (result + ord(element) * degree[i]) % p
    return result
