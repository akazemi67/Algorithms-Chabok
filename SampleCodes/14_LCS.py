def recover_lcs(S, T, lcs):
    n, m = len(S), len(T)
    res = []
    while n > 0 and m > 0:
        if S[n - 1] == T[m - 1]:
            res.append(S[n - 1])
            n -= 1
            m -= 1
        elif lcs[n - 1][m] > lcs[n][m - 1]:
            n -= 1
        else:
            m -= 1
    return ''.join(res[::-1])


def longest_common_subsequence(S, T):
    n, m = len(S), len(T)
    lcs = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs[n][m], recover_lcs(S, T, lcs)


s1 = "AUHFJWOFNMRKCHWPFVNJHWYH"
s2 = "AQWSFBCWOBBCNMKHOLPOVQQJHKWY"
print(longest_common_subsequence(s1, s2))
