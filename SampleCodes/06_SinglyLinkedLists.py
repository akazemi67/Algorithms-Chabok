class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node

    def add_tail(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
        self.tail = node

        if not self.head:
            self.head = node

    def del_head(self):
        if not self.head:
            return None

        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None

        return data

    def del_tail(self):
        if not self.head:
            return None

        temp = self.head
        while temp.next and temp.next != self.tail:
            temp = temp.next

        # We have only one item
        if not temp.next:
            return self.del_head()

        data = self.tail.data
        temp.next = None
        self.tail = temp
        return data

    def del_data(self, data):
        if not self.head:
            return False

        prev_temp = self.head
        temp = self.head
        while temp and temp.data != data:
            prev_temp = temp
            temp = temp.next

        if not temp:
            return False

        prev_temp.next = temp.next
        if self.tail == temp:
            self.tail = prev_temp

        if self.head == temp:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        return True

    def print_list(self):
        if not self.head:
            print("Empty List.")
            return

        items = []
        temp = self.head
        while temp:
            items.append(temp.data)
            temp = temp.next

        print('List: ', ' -> '.join(items))


def test_singly_list():
    list = SinglyLinkedList()
    list.print_list()

    list.add_head("A")
    list.print_list()
    list.del_tail()
    list.print_list()

    list.add_tail("X")
    list.print_list()
    list.del_data("X")
    list.print_list()

    list.add_head("B")
    list.add_head("C")
    list.add_tail("D")
    list.add_tail("E")
    list.add_head("F")
    list.print_list()

    list.del_data("F")
    list.print_list()

    list.del_data("E")
    list.print_list()

    list.del_head()
    list.add_head("X")
    list.del_tail()
    list.add_tail("Y")
    list.print_list()


if __name__ == "__main__":
    test_singly_list()
