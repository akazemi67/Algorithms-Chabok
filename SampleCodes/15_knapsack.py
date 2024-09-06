def select_items(i, dp, items, W, selected):
    if i == 0 or W == 0:
        return
    if dp[i][W] > dp[i - 1][W]:
        selected.append(i)
        return select_items(i - 1, dp, items, W - items[i - 1][1], selected)
    return select_items(i - 1, dp, items, W, selected)


def knapsack(items, W):
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        vi, wi = items[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if w >= wi:
                dp[i][w] = max(dp[i - 1][w], vi + dp[i - 1][w - wi])

    selected = []
    select_items(n, dp, items, W, selected)
    return dp[n][W], selected[::-1]


# value, weight
items = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)]
W = 11
print(knapsack(items, W))
