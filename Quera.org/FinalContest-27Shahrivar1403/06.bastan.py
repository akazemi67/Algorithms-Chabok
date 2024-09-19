# Problem's Link: https://quera.org/problemset/1362

n = int(input())
ways = input()
dp = [0] * n
dp[0] = 1

for w in range(1, n):
    if ways[w - 1] != 'T':
        dp[w] += dp[w - 1]
    if w - 2 >= 0 and ways[w - 2] != 'T':
        dp[w] += dp[w - 2]
    if w - 3 >= 0 and ways[w - 3] != 'T':
        dp[w] += dp[w - 3]

print(dp[n - 1])
