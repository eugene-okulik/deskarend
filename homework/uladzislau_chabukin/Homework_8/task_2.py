import sys


def fibonacci(num):
    fib_1, fib_2 = 0, 1
    for _ in range(num):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


sys.set_int_max_str_digits(100000)

count = 1
for fib in fibonacci(200_000):
    if count in (5, 200, 1000, 100_000):
        print(fib)
    count += 1
