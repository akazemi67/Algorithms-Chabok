# Problem's Link: https://codeforces.com/contest/1243/problem/A

tc = int(input())
while tc > 0:
    n = int(input())
    arr = sorted(map(int, input().split()))
    ans = 0
    
    for i in range(n):
        curr = min(arr[i], n-i)
        ans = max(ans, curr)
    
    print(ans)
    tc -= 1

