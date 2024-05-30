class ArrayQueue:
    def __init__(self, max_size):
        max_size += 1
        self.items = [0] * max_size
        self.front = 0
        self.back = 0
        self.max_size = max_size

    def __next(self):
        return (self.back + 1) % self.max_size

    def put(self, data):
        nxt = self.__next()
        if nxt == self.front:
            return False

        self.items[self.back] = data
        self.back = nxt
        return True

    def get(self):
        if self.front == self.back:
            return None

        data = self.items[self.front]
        self.front = (self.front + 1) % self.max_size
        return data

    def is_empty(self):
        return self.front == self.back


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.front = None
        self.back = None

    def put(self, data):
        node = Node(data)
        if not self.back:
            self.back = node
            self.front = node
        else:
            self.back.next = node
            self.back = node
        return True

    def get(self):
        if not self.front:
            return None
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.back = None
        return data

    def is_empty(self):
        return self.front is None


def test_queue(array=True):
    q = None
    if array:
        q = ArrayQueue(5)
    else:
        q = LinkedListStack()
    print(type(q))

    items = [1, 2, 3, 4, 5, 6, 7]
    for i in items:
        if not q.put(i):
            print(f"Could not insert {i} into q.")
            break

    got = []
    while not q.is_empty():
        got.append(q.get())

    q.put(10)
    q.put(11)
    got.append(q.get())
    got.append(q.get())
    print(' -> '.join(map(str, got)))


if __name__ == "__main__":
    test_queue()
    print("---------------------------")
    test_queue(False)
