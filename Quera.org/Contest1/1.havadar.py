# Problem's Link: https://quera.org/problemset/176776

s = input()

res = 0
cnt = 0
for c in s:
    if c == '1':
        cnt = 0
    else:
        cnt += 1
        res = cnt if cnt > res else res

print(res)
