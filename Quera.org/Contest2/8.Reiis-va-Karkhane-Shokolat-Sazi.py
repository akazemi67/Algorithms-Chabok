# Problem's Link: https://quera.org/problemset/20251

def solve(tree, u):
    if not u in tree:
        return (0, 1)

    result, cnt = 0, 0
    for v in tree[u]:
        r, c = solve(tree, v)
        result += r + c
        cnt += c
    return (result, cnt + 1)


n = int(input())
pi = list(map(int, input().split()))

tree = {}
for i in range(n-1):
    u = i+2
    v = pi[i]
    if v in tree:
        tree[v].append(u)
    else:
        tree[v] = [u]


print(sum(solve(tree, 1)))
