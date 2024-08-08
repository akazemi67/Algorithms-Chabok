# Problem's Link: https://quera.org/problemset/658

n = int(input())
values = list(map(int, input().split()))

result = 0
curr = 0
for v in values:
    curr += v
    if curr < 0:
        curr = 0
    result = max(result, curr)

print(result)
