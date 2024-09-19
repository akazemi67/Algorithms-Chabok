# Problem's Link: https://quera.org/problemset/9734
from collections import defaultdict


def dfs(u, graph, visited, topo):
    if visited[u]:
        return

    visited[u] = True
    if u in graph:
        for v in graph[u]:
            dfs(v, graph, visited, topo)
    topo.append(u)


while True:
    n = int(input())
    if n == 0:
        break

    graph = {}
    indegs = defaultdict(int)
    for u in range(1, n + 1):
        deps = list(map(int, input().split()))
        graph[u] = deps[1:]
        for u in graph[u]:
            indegs[u] += 1

    q = []
    topo = []
    for u in range(1, n + 1):
        if indegs[u] == 0:
            q.append(u)

    max_deps = [0, 0]
    while len(q) > 0:
        u = q.pop(0)
        visited = [False] * (n + 1)
        topo = []
        dfs(u, graph, visited, topo)

        if len(topo) > max_deps[0]:
            max_deps = [len(topo), u]

    print(max_deps[1])

