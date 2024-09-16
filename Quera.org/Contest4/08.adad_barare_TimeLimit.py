# Problem's Link: https://quera.org/problemset/10168

MAX = 10**7

a, b = map(int, input().split())
dp = [MAX]*(b+5)
dp[a] = 0

if a==2 or a==3:
    dp[2*a] = 1

for num in range(a, b+1):
    if dp[num]>=MAX:
        continue

    p = 2
    while p*p<=num:
        if num%p==0:
            nn = num + p
            if nn<=b:
                dp[nn] = min(dp[nn], 1+dp[num])
                
            nn = num + num//p
            if nn<=b:
                dp[nn] = min(dp[nn], 1+dp[num])
        p += 1

        
if dp[b]<MAX:
    print(dp[b])
else:
    print(-1)

