# Problem's Link: https://codeforces.com/contest/115/problem/A

import sys

sys.setrecursionlimit(2500)
links = {}
roots = set()

def solve(u):
    if not u in links:
        return 1
    
    res = 0
    for v in links[u]:
        res = max(res, solve(v))
    return res+1


n = int(input())
for to in range(1, n+1):
    fr = int(input())
    if fr > 0:
        if fr in links:
            links[fr].append(to)
        else:
            links[fr] = [to]
    else:
        roots.add(to)

res = 0
for u in roots:
    res = max(res, solve(u))
    
print(res)

