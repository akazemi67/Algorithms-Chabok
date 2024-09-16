# Problem's Link: https://quera.org/problemset/8527

n = int(input())
hi = list(map(int, input().split()))

max_right = hi[::]
i = n-2
while i>=0:
    max_right[i] = max(max_right[i+1], max_right[i])
    i -= 1  

max_left = hi[::]
i = 1
while i<n:
    max_left[i] = max(max_left[i-1], max_left[i])
    i += 1

res = 0
for i in range(n):
    a = hi[i]
    b = min(max_left[i], max_right[i])
    res += max(a, b) - hi[i]

print(res)

