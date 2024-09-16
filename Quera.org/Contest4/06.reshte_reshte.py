# Problem's Link: https://quera.org/problemset/108670


def are_similar(s1, s2):
    if s1.lower() == s2.lower():
        return 1

    n, m = len(s1), len(s2)
    if n < m:
        n, m = m, n
        s1, s2 = s2, s1
    if n - m > 1:
        return 0

    for i in range(n):
        s1t = s1[0:i] + s1[i + 1:]
        if s1t == s2:
            return 1
    if n != m:
        return 0

    diffs = 0
    for i in range(n):
        if s1[i] != s2[i]:
            diffs += 1

    return 1 if diffs == 1 else 0


n, k = map(int, input().split())
words = []
for _ in range(n):
    words.append(input())

for _ in range(k):
    candid = input()
    res = 0
    for w in words:
        res += are_similar(candid, w)
    print(res)

