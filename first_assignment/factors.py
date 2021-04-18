import math

def get_factors(number):
    factors = []
    # Print the number of two's that divide n
    while number % 2 == 0:
        factors.append(2)
        number = number / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(number)) + 1, 2):

        # while i divides n , print i ad divide n
        while number % i == 0:
            factors.append(i)
            number = number / i

    # Condition if n is a prime
    # number greater than 2
    if number > 2:
        factors.append(number)
    return factors

print(get_factors(150))
