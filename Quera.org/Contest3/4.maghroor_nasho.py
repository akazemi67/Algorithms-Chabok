# Problem's Link: https://quera.org/problemset/33046


def add_edge(edges, u, v):
    if u in edges:
        edges[u].append(v)
    else:
        edges[u] = [v]


n = int(input())
edges = {}
for i in range(n-1):
    u, v = map(int, input().split())
    add_edge(edges, u, v)
    add_edge(edges, v, u)

colors = 0
for u in range(1, n+1):
    if u in edges:
        colors = max(colors, len(edges[u]))
print(colors)
