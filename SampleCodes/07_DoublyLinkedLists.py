class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        self.head = node

    def add_tail(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node

    def __remove_node(self, node):
        ni = node.next
        pi = node.prev
        ni.prev = pi
        pi.next = ni

    def __has_one_item(self):
        return self.head.next == self.head

    def del_head(self):
        if not self.head:
            return None
        data = self.head.data

        if self.__has_one_item():
            self.head = None
        else:
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next

        return data

    def del_tail(self):
        if not self.head:
            return None
        tail = self.head.prev

        if self.__has_one_item():
            self.head = None
        else:
            self.__remove_node(tail)

        return tail.data

    def del_data(self, data):
        if not self.head:
            return False

        temp = self.head
        while True:
            if temp.data == data:
                if temp == self.head:
                    self.del_head()
                else:
                    self.__remove_node(temp)
                break

            temp = temp.next
            if temp == self.head:
                return False

        return True

    def print_list(self):
        if not self.head:
            print("Empty List!")
            return

        temp = self.head
        items = []
        while True:
            items.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break

        print(" --> ".join(items))


def test_doubly_list():
    list = DoublyLinkedList()
    list.print_list()
    list.add_head("A")
    list.add_tail("B")
    list.add_head("C")
    list.del_data("C")
    list.add_tail("D")
    list.print_list()

    list.del_data("B")
    list.print_list()

    list.del_tail()
    list.print_list()

    list.del_head()
    list.print_list()

    list.del_tail()
    list.print_list()

    list.add_head("X")
    list.add_tail("Y")
    list.add_head("Z")
    list.print_list()
    print("DONE!")


if __name__ == "__main__":
    test_doubly_list()
