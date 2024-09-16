# Problem's Link: https://quera.org/problemset/170167

import decimal
decimal.setcontext(decimal.Context(prec=25))

n = int(input())
arr = [ decimal.Decimal(x) for x in  input().split() ]
prev = decimal.Decimal(0)
i = n-1

while i>=0:
    arr[i] += prev
    parts = 0

    if i>0:
        parts = arr[i]/decimal.Decimal(i)
    prev += parts
    i -= 1

for i in range(n):
    print(f"{arr[i]:.5f}", end=' ')

