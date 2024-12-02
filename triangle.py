side_a = input('a: ')
side_b = input('b: ')
side_c = input('c: ')

if side_a == side_b == side_c:
    print('Равностронний треугольник')
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print('Равнобедренный треугольник')
else:
    result_3 = print('Разносторонний треугольник')
