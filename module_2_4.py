numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_prime = []
for j in numbers:
    is_prime = True
    for i in range(2, j // 2):
        if j % i == 0:
            is_prime = False
            break
    if is_prime:
        if j != 1:
            primes.append(j)
    else:
        not_prime.append(j)
print("Простые числа:", primes)
print("Составные числа:", not_prime)