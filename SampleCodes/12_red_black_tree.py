RED = True
BLACK = False


class BstNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = RED
        self.n = 1


class RedBlackBST:
    def __init__(self):
        self.root = None

    def isRed(self, node):
        if not node:
            return BLACK
        return node.color == RED

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        node.n = self.__size(node.left) + self.__size(node.right) + 1
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        node.n = self.__size(node.left) + self.__size(node.right) + 1
        return x

    def flip_colors(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def __put(self, node, key, value):
        if not node:
            return BstNode(key, value)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.value = value

        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotate_left(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotate_right(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flip_colors(node)

        node.n = self.__size(node.left) + self.__size(node.right) + 1
        return node

    def put(self, key, value):
        self.root = self.__put(self.root, key, value)
        self.root.color = BLACK

    def __size(self, node):
        if not node:
            return 0
        l = self.__size(node.left)
        r = self.__size(node.right)
        return l + r + 1

    def size(self):
        return self.__size(self.root)

    def __rank(self, node, key):
        '''
        Number of items in the tree that are less than key.
        '''
        if not node:
            return 0
        if key > node.key:
            res = 0
            if node.left:
                res = node.left.n
            return 1 + res + self.__rank(node.right, key)
        if key < node.key:
            return self.__rank(node.left, key)

        if not node.left:
            return 0
        return node.left.n

    def rank(self, key):
        return self.__rank(self.root, key)

    def __in_order(self, node):
        if not node:
            return
        self.__in_order(node.left)
        print(node.key, end='  ')
        self.__in_order(node.right)

    def print_inorder(self):
        print("InOrder: ", end='')
        self.__in_order(self.root)
        print()

    def __pre_order(self, node):
        if not node:
            return
        print(node.key, end='  ')
        self.__pre_order(node.left)
        self.__pre_order(node.right)

    def print_preorder(self):
        print("PreOrder: ", end='')
        self.__pre_order(self.root)
        print()

    def __calc_height(self, node):
        if not node:
            return 0
        l = self.__calc_height(node.left)
        r = self.__calc_height(node.right)
        return max(l, r) + 1

    def height(self):
        return self.__calc_height(self.root)


if __name__ == "__main__":
    bst = RedBlackBST()
    bst.put(2, "A")
    bst.put(3, "B")
    bst.put(4, "C")
    bst.put(12, "D")
    bst.put(15, "E")
    bst.put(20, "F")
    bst.put(25, "G")
    bst.put(30, "H")
    bst.put(10, "I")
    bst.put(40, "J")
    bst.print_inorder()
    bst.print_preorder()
    print("Rank 8: ", bst.rank(8))
    print("Height: ", bst.height())
