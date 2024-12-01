def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        num = []
        for j in range(m):
            num.append(value)
        matrix.append(num)
    return matrix

result1 = get_matrix(2, 2, 2)
result2 = get_matrix(3, 4, 6)
result3 = get_matrix(5, 6, 3)
print(result1)
print(result2)
print(result3)
