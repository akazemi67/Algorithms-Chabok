# Problem's Link: https://codeforces.com/contest/1243/problem/B1


tc = int(input())
while tc > 0:
    n = int(input())
    s1 = input()
    s2 = input()
    
    diffs = []
    for i in range(n):
        if s1[i]!=s2[i]:
            diffs.append(i)
            
    poss = False
    if len(diffs)==2:
        i, j = diffs
        if s1[i]==s1[j] and s2[i]==s2[j]:
            poss = True
    
    print("Yes" if poss else "No")
    tc -= 1

