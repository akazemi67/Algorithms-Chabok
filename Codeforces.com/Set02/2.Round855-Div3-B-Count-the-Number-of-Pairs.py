# Problem's Link: https://codeforces.com/contest/1800/problem/B

from collections import defaultdict


def solve(st, n, k):
    letters = defaultdict(int)
    for c in st:
        letters[c] += 1
    
    res = 0
    for i in range(26):
        sl = chr(ord('a') + i)
        bl = chr(ord('A') + i)
        
        sc = letters[sl]
        bc = letters[bl]
        diff = max(sc, bc) - min(sc, bc)
        
        res += min(sc, bc)
        if k > 0:
            op = min(k, diff//2)
            k -= op
            res += op
            
    return res


t = int(input())
while t>0:
    n, k = map(int, input().split())
    st = input()
    print(solve(st, n, k))
    t -= 1
