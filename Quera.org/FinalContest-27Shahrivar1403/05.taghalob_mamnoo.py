# Problem's Link: https://quera.org/problemset/8940

def group_strings(strings, s, p, q):
    ss = s[:p] + s[-q:]
    if ss in strings:
        strings[ss] += 1
    else:
        strings[ss] = 1


n, p, q = map(int, input().split())
strings = {}
for _ in range(n):
    s = input()
    group_strings(strings, s, p, q)

print(len(strings))
