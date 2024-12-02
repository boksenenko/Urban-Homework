a = input('a: ')
b = input('b: ')
c = input('c: ')

if a >= b and b >= c:
    print(b)
elif b >= a and a >= c:
    print(a)
elif c >= b and b >= a:
    print(b)
else:
    print(c)