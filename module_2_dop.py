from random import randint

num_1 = randint(3, 20)
print(num_1)
list_1 = []

for i in range(1, num_1):
    for j in range(2, 20):
        res_1 = i + j
        if num_1 % res_1 == 0 and i != j and i < j:
            list_1 += i, j

print(list_1)