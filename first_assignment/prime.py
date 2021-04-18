import math


def get_prime_numbers_up_to(n):
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(get_prime_numbers_up_to(100))
