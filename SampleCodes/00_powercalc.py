import sys
import timeit


def dummy_pow(a, n):
    res = 1
    while n > 0:
        res *= a
        n -= 1
    return res


def good_pow(a, n):
    if n == 0:
        return 1
    res = good_pow(a, n // 2)
    if n % 2 == 0:
        return res * res
    return a * res * res


sys.set_int_max_str_digits(0)
sys.setrecursionlimit(1500)

start = timeit.default_timer()
print(dummy_pow(2, (1 << 19)))
end = timeit.default_timer()
print(f"Dummy Runtime = {end - start}")

start = timeit.default_timer()
res = good_pow(2, (1 << 19))
print(f"-> 2^(2^19) has {len(str(res))} digits.")
end = timeit.default_timer()
print(f"Good Runtime = {end - start}")
