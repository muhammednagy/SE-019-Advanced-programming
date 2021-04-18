def reverseFibonacci(n):
    fib_list = []
    a = [0] * n

    # assigning first and second elements
    a[0] = 0
    a[1] = 1

    for i in range(2, n):
        # storing sum in the
        # preceding location
        a[i] = a[i - 2] + a[i - 1]

    for i in range(n - 1, -1, -1):
        # printing array in
        # reverse order
        fib_list.append(a[i])

    return fib_list

print(reverseFibonacci(10))