first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('И ещё одно: ')

if first == second and first == third :
    print (3)
elif first == second or first == third :
    print(2)
else :
    print(0)