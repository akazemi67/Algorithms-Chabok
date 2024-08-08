# Problem's Link: https://codeforces.com/contest/1800/problem/D

def solve(st, n):
    eq = 0
    for i in range(n-2):
        if st[i]==st[i+2]:
            eq += 1
    return n-1-eq


t = int(input())
while t>0:
    n = int(input())
    st = input()
    print(solve(st, n))
    t -= 1

