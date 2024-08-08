# Problem's Link: https://quera.org/problemset/603

dp = {1: 1, 2: 2, 3: 3, 4: 5, 5: 9}


def calc(n):
    if n < 0:
        return 0
    if n in dp:
        return dp[n]

    res = calc(n - 1) + calc(n - 2) + calc(n - 5)
    dp[n] = res
    return res


n = int(input())
print(calc(n))
