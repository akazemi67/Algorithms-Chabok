# Problem's Link: https://quera.org/problemset/3410

memo = [ [0]*101 for _ in range(101) ]
def calc(n, k):
    if n==0 or k==0 or n==k:
        return 1
    if memo[n][k] > 0:
        return memo[n][k]
        
    res = calc(n-1, k) + calc(n-1, k-1)
    memo[n][k] = res
    return res


m = int(input())
for n in range(m):
    for k in range(n+1):
        print(calc(n, k), end=' ')
    print()
