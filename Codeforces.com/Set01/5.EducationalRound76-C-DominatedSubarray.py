# Problem's Link: https://codeforces.com/contest/1257/problem/C

tc = int(input())
while tc > 0:
    n = int(input())
    arr = [ (int(x), i) for i,x in enumerate(input().split()) ]
    sarr = sorted(arr)
    
    ans = 10**10
    for idx in range(1, n):
        if sarr[idx][0]==sarr[idx-1][0]:
            ans = min(ans, sarr[idx][1]-sarr[idx-1][1]+1)
        
    print( -1 if ans==10**10 else ans )
    tc -= 1

