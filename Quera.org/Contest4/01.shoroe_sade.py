# Problem's Link: https://quera.org/problemset/9719

import string

digs = string.digits + string.ascii_letters.upper()

def to_base(num, b):
    res = ''
    while num>0:
        res += digs[num%b]
        num //= b
    return res[::-1]


base = int(input())
for n in range(1, 300):
    n2b = to_base(n*n, base)
    if n2b == n2b[::-1]:
        nb = to_base(n, base)
        print(nb, n2b)

