# Problem's Link: https://codeforces.com/problemset/problem/1843/C

def solve(n):
    res = 0
    while n > 0:
        res += n
        n = n//2
    return res
    

t = int(input())
while t>0:
    n = int(input())
    print(solve(n))
    t -= 1
    
