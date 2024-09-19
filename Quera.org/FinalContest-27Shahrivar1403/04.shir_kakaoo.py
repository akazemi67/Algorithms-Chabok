# Problem's Link: https://quera.org/problemset/6395

input()
values = map(int, input().split())
want = 0
res = 0
for v in values:
    want += v
    res = max(res, want)

print(res)

