from time import time

start = time()

def fib1(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib1(x-1) + fib1(x-2)

print(fib1(35), time() - start)

start = time()

def fib2(x):
    def calcfib(n, a, b):
        if n == 0:
            return a
        else:
            return calcfib(n-1, b, a+b)
    return calcfib(x, 0, 1)

print(fib2(35), time() - start)
