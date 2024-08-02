class MaxPQ:
    def __init__(self):
        self.N = 0
        self.items = [0]

    def __bottom_up_reheapify(self, k):
        while k > 1 and self.items[k // 2] < self.items[k]:
            i = k // 2
            self.items[i], self.items[k] = self.items[k], self.items[i]
            k = i

    def __top_down__reheapify(self, k):
        while 2 * k <= self.N:
            i = 2 * k
            if i < self.N and self.items[i + 1] > self.items[i]:
                i += 1
            if self.items[k] > self.items[i]:
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

    def delete_max(self):
        if self.N == 0:
            return None
        max = self.items[1]
        self.items[1] = self.items[self.N]
        self.items[self.N] = None
        self.N -= 1
        self.__top_down__reheapify(1)
        return max


if __name__ == "__main__":
    pq = MaxPQ()
    pq.insert(2)
    pq.insert(5)
    pq.insert(4)
    pq.insert(7)
    pq.insert(6)

    for i in range(3):
        print(pq.delete_max())

    print("After inserting new items:")
    pq.insert(8)
    pq.insert(3)
    pq.insert(10)
    pq.insert(1)

    while not pq.is_empty():
        print(pq.delete_max())
