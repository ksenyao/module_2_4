numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    if num > 1:
        primes.append(num)
        is_prime = True
        for d in range(2, num):
            if num % d == 0:
                not_primes.append(num)
            is_prime = False
            break
print(primes)
print(not_primes)
