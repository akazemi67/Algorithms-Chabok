class BstNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def __put(self, node, key, value):
        if not node:
            return BstNode(key, value)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.value = value
        return node

    def put(self, key, value):
        self.root = self.__put(self.root, key, value)

    def __get(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self.__get(node.left, key)
        return self.__get(node.right, key)

    def get(self, key):
        return self.__get(self.root, key)

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

    def __min(self, node):
        if not node:
            return None
        if not node.left:
            return node
        return self.__min(node.left)

    def min(self):
        min_item = self.__min(self.root)
        if not min_item:
            return None
        return min_item.key

    def __max(self, node):
        if not node:
            return None
        if not node.right:
            return node
        return self.__max(node.right)

    def max(self):
        max_item = self.__max(self.root)
        if not max_item:
            return None
        return max_item.key

    def __size(self, node):
        if not node:
            return 0
        l = self.__size(node.left)
        r = self.__size(node.right)
        return l + r + 1

    def size(self):
        return self.__size(self.root)

    def __select(self, node, cnt):
        '''
        Returns the node in the tree that has cnt items less nodes
        '''
        if not node:
            return None
        less_count = self.__size(node.left)
        if less_count > cnt:
            return self.__select(node.left, cnt)
        if less_count < cnt:
            return self.__select(node.right, cnt - less_count - 1)
        return node

    def select(self, cnt):
        res_node = self.__select(self.root, cnt)
        if not res_node:
            return None
        return res_node.key

    def __rank(self, node, key):
        '''
        Number of items in the tree that are less than key.
        '''
        if not node:
            return 0
        if key > node.key:
            return 1 + self.__size(node.left) + self.__rank(node.right, key)
        if key < node.key:
            return self.__rank(node.left, key)
        return self.__size(node.left)

    def rank(self, key):
        return self.__rank(self.root, key)

    def __delete_min(self, node):
        if not node:
            return None
        if not node.left:
            return node.right
        node.left = self.__delete_min(node.left)
        return node

    def delete_min(self):
        self.root = self.__delete_min(self.root)

    def __delete(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self.__delete(node.left, key)
        elif key > node.key:
            node.right = self.__delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            temp = node
            node = self.__min(temp.right)
            node.right = self.__delete_min(temp.right)
            node.left = temp.left
        return node

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __calc_height(self, node):
        if not node:
            return 0
        l = self.__calc_height(node.left)
        r = self.__calc_height(node.right)
        return max(l, r) + 1

    def height(self):
        return self.__calc_height(self.root)

if __name__ == "__main__":
    bst = BST()
    bst.put(10, "A")
    bst.put(2, "B")
    bst.put(11, "C")
    bst.put(8, "D")
    bst.put(15, "E")
    bst.put(12, "F")
    bst.put(4, "G")
    bst.put(1, "H")
    bst.print_inorder()
    bst.print_preorder()
    print("Min Key: ", bst.min())
    print("Max Key: ", bst.max())
    print("Select 5: ", bst.select(5))
    print("Rank 8: ", bst.rank(8))

    bst.delete_min()
    bst.delete_min()
    print("\n** After 2 Delete Mins **")
    bst.print_inorder()
    bst.print_preorder()

    bst.put(7, "I")
    bst.put(16, "J")
    print("\n ** After Adding 7, 16 **")
    bst.print_inorder()
    bst.print_preorder()

    bst.delete(4)
    bst.delete(10)
    bst.delete(8)
    print("\n ** After Deleting 4,10,8 **")
    bst.print_inorder()
    bst.print_preorder()
