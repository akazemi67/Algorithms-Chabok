class MinPQ:
    def __init__(self, n):
        self.N = 0
        self.items = [(0, 0)] * n  # value, vertex

    def __bottom_up_reheapify(self, k):
        while k > 1 and self.items[k // 2][0] > self.items[k][0]:
            i = k // 2
            self.items[i], self.items[k] = self.items[k], self.items[i]
            k = i

    def __top_down__reheapify(self, k):
        while 2 * k <= self.N:
            i = 2 * k
            if i < self.N and self.items[i + 1][0] < self.items[i][0]:
                i += 1
            if self.items[k][0] <= self.items[i][0]:
                break
            self.items[k], self.items[i] = self.items[i], self.items[k]
            k = i

    def is_empty(self):
        return self.N == 0

    def size(self):
        return self.N

    def insert(self, value):
        self.N += 1
        if len(self.items) <= self.N:
            self.items.append(value)
        else:
            self.items[self.N] = value
        self.__bottom_up_reheapify(self.N)

    def delete_min(self):
        if self.N == 0:
            return None
        max = self.items[1]
        self.items[1] = self.items[self.N]
        self.items[self.N] = None
        self.N -= 1
        self.__top_down__reheapify(1)
        return max


def add_to_pq(u, graph, pq):
    for e in graph[u]:
        pq.insert(e)


if __name__ == "__main__":
    # (weight, vertex)
    graph = {}
    graph[0] = [(30, 1, 0), (10, 2, 0), (40, 3, 0)]
    graph[1] = [(30, 0, 1), (60, 2, 1), (20, 3, 1)]
    graph[2] = [(10, 0, 2), (60, 1, 2), (50, 4, 2)]
    graph[3] = [(40, 0, 3), (20, 1, 3), (30, 4, 3)]
    graph[4] = [(50, 2, 4), (30, 3, 4)]

    # Running Prim's Algorithm
    selected_edges = []
    marked_vertices = set([0])
    pq = MinPQ(10)
    add_to_pq(0, graph, pq)

    while not pq.is_empty():
        e = pq.delete_min()
        if not e[1] in marked_vertices:
            marked_vertices.add(e[1])
            add_to_pq(e[1], graph, pq)
            selected_edges.append(e)

    print("\n-------------\nSelected Edges:")
    for e in selected_edges:
        print(e)
