# Problem's Link: https://quera.org/problemset/28948

s = input()
res = []

for c in s:
    if c == '=':
        if len(res) > 0:
            res.pop()
    else:
        res.append(c)

print(''.join(res))

