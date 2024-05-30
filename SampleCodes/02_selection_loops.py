n = 20
res = 0
for i in range(n):
    for j in range(i + 1, n):
        res += 1

print(f"Res = {res}")
print(f"n*(n-1)/2 = {n * (n - 1) // 2}")
