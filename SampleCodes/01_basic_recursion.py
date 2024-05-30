def prnt(n):
    if n <= 0:
        return
    print(n)
    prnt(n - 1)
    print(n)


def fib(n):
    if n <= 1:
        return n

    n1 = fib(n - 1)
    n2 = fib(n - 2)
    return n1 + n2


# prnt(5)
print(fib(3))
