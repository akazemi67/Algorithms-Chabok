class ArrayStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [0] * max_size
        self.top = -1

    def push(self, data):
        self.top += 1
        self.items[self.top] = data

    def pop(self):
        if self.top < 0:
            return None
        data = self.items[self.top]
        self.top -= 1
        return data

    def print_top(self):
        if self.top < 0:
            print("Empty Stack.")
            return
        print(f"Top: {self.items[self.top]}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None
        top = self.top
        self.top = top.next
        top.next = None
        return top.data

    def print_top(self):
        if not self.top:
            print("Empty Stack!")
            return
        print(f"Top: {self.top.data}")


def test_stack(array=True):
    stack = None
    if array:
        stack = ArrayStack(10)
    else:
        stack = LinkedListStack()
    print(type(stack))
    stack.print_top()

    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.print_top()

    stack.pop()
    stack.pop()
    stack.print_top()

    stack.pop()
    stack.print_top()


if __name__ == "__main__":
    test_stack()
    print("----------------------")
    test_stack(False)
