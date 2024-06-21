class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self):
        self.root = None

    def new_root_left(self, data):
        node = TreeNode(data)
        node.left = self.root
        self.root = node
        return node

    def new_root_right(self, data):
        node = TreeNode(data)
        node.right = self.root
        self.root = node
        return node

    def add_left_parent(self, parent, data):
        node = TreeNode(data)
        parent.left = node
        return node

    def add_right_parent(self, parent, data):
        node = TreeNode(data)
        parent.right = node
        return node

    def __in_order(self, node):
        if not node:
            return
        self.__in_order(node.left)
        print(node.data, end='  ')
        self.__in_order(node.right)

    def __pre_order(self, node):
        if not node:
            return
        print(node.data, end='  ')
        self.__pre_order(node.left)
        self.__pre_order(node.right)

    def __post_order(self, node):
        if not node:
            return
        self.__post_order(node.left)
        self.__post_order(node.right)
        print(node.data, end='  ')

    def print_preorder(self):
        print("\nPreOrder: ", end='')
        self.__pre_order(self.root)

    def print_inorder(self):
        print("\nInoder: ", end='')
        self.__in_order(self.root)

    def print_postoder(self):
        print("\nPostOrder: ", end='')
        self.__post_order(self.root)

    def __calc_height(self, node):
        if not node:
            return 0
        l = self.__calc_height(node.left)
        r = self.__calc_height(node.right)
        return max(l, r) + 1

    def height(self):
        return self.__calc_height(self.root)

    def __count_nodes(self, node):
        if not node:
            return 0
        l = self.__count_nodes(node.left)
        r = self.__count_nodes(node.right)
        return l + r + 1

    def nodes(self):
        return self.__count_nodes(self.root)

    def __search(self, node, x):
        if not node:
            return False
        if node.data == x:
            return True
        return self.__search(node.left, x) or \
            self.__search(node.right, x)

    def search(self, x):
        return self.__search(self.root, x)

    def __count_leaves(self, node):
        if not node:
            return 0
        if (not node.left) and (not node.right):
            return 1
        l = self.__count_leaves(node.left)
        r = self.__count_leaves(node.right)
        return l + r

    def leaves(self):
        return self.__count_leaves(self.root)


if __name__ == "__main__":
    tree = Tree()
    tree.new_root_left(7)
    tree.new_root_right(6)
    node = tree.new_root_right(3)
    tree.add_left_parent(node, 1)
    node = tree.new_root_left(8)
    node = tree.add_right_parent(node, 10)
    tree.add_right_parent(node, 14)
    tree.print_inorder()
    tree.print_preorder()
    tree.print_postoder()
    print()
    print("Height: ", tree.height())
    print("Nodes: ", tree.nodes())
    print("Leaves: ", tree.leaves())
    print("Search 7: ", tree.search(7))
    print("Search 10: ", tree.search(10))
    print("Search 20: ", tree.search(20))
