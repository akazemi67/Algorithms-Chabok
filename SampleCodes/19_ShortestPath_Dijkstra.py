from heapq import heapify, heappush, heappop


def shortest_distances(graph, source):
    distances = {node: float("inf") for node in graph}
    distances[source] = 0

    pq = [(0, source)]
    heapify(pq)
    visited = set()

    while pq:
        current_distance, current_node = heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            dist = current_distance + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heappush(pq, (dist, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        "A": {"B": 3, "C": 3},
        "B": {"A": 3, "D": 3.5, "E": 2.8},
        "C": {"A": 3, "E": 2.8, "F": 3.5},
        "D": {"B": 3.5, "E": 3.1, "G": 10},
        "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
        "F": {"G": 2.5, "C": 3.5},
        "G": {"F": 2.5, "E": 7, "D": 10},
    }

    print(shortest_distances(graph, "A"))
