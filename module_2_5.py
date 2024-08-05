def get_matrix(n, m, value):
    return [[value for _ in range(m)] for _ in range(n)]
result1 = get_matrix(3, 4, 22)
result2 = get_matrix(2,3, 10)
result3 = get_matrix(5, 6, 88)
print(result1)
print(result2)
print(result3)