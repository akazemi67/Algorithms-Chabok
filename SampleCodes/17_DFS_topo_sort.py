def dfs_topo(u, graph, visited, topo):
    if visited[u]:
        return
    visited[u] = True
    if u in graph:
        for v in graph[u]:
            dfs_topo(v, graph, visited, topo)
    topo.append(u)


n = 7
graph = {}
graph[0] = [1, 2, 5]
graph[1] = [4]
graph[2] = []
graph[3] = [2, 4, 5, 6]
graph[4] = []
graph[5] = [2]
graph[6] = [0, 4]
visited = [False] * n
topo_sort = []

for u in range(n):
    if not visited[u]:
        dfs_topo(u, graph, visited, topo_sort)

print("Topo Sort: ", topo_sort[::-1])
