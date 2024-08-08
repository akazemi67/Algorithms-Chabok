# Problem's Link: https://codeforces.com/contest/1253/problem/A


tc = int(input())
while tc > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    barr = list(map(int, input().split()))
    
    poss = True
    diff_range = 0
    diff = 0
    for i in range(n):
        if not poss:
            break
        
        if arr[i]!=barr[i]:
            if diff_range==0:
                diff_range = 1
                
                diff = barr[i] - arr[i]
                if diff<0:
                    poss = False
            elif diff_range>1 or (diff_range==1 and (barr[i]-arr[i])!=diff):
                poss = False
                
        elif diff_range>0:
            diff_range += 1
    
    print("YES" if poss else "NO")
    
    tc -= 1

