# Problem's Link: https://quera.org/problemset/9759


def index(pos):
    if 'a' <= pos <= 'z':
        return ord(pos) - ord('a')
    return ord(pos) - ord('A') + 30


roads = [[10 ** 8] * 60 for _ in range(60)]
cows = set()
m = int(input())
for _ in range(m):
    fr, to, cost = input().split()
    u, v = index(fr), index(to)
    if 'A' <= fr < 'Z':
        cows.add(fr)
    if 'A' <= to < 'Z':
        cows.add(to)
    roads[u][v] = roads[v][u] = min(roads[u][v], int(cost))


for k in range(60):
    for u in range(60):
        for v in range(60):
            roads[u][v] = min(roads[u][v], roads[u][k] + roads[k][v])


best_cow = ''
best_cost = 10 ** 8
dest = index('Z')
for c in cows:
    u = index(c)
    if roads[u][dest] < best_cost:
        best_cost = roads[u][dest]
        best_cow = c

print(best_cow, best_cost)

