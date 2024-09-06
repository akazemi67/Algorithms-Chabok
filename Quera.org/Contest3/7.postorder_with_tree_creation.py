# Problem's Link: https://quera.org/problemset/356

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.preidx = 0

    def __build_tree(self, preorder, fr, to, inorder_indices):
        if fr > to:
            return None         

        node = TreeNode(preorder[self.preidx])
        self.preidx += 1

        inidx = inorder_indices[node.value]
        node.left = self.__build_tree(preorder, fr, inidx-1, inorder_indices)
        node.right = self.__build_tree(preorder, inidx+1, to, inorder_indices)

        return node

    def build_tree(self, preorder, fr, to, inorder_indices):
        self.root = self.__build_tree(preorder, fr, to, inorder_indices)

    def __post(self, node):
        if not node:
            return 
        self.__post(node.left)
        self.__post(node.right)
        print(node.value, end=' ')

    def post_order(self):
        self.__post(self.root)


n = int(input())
inorder = input().split()
preorder = input().split()

in_indices = {}
for i in range(n):
    in_indices[inorder[i]] = i

tree = Tree()
tree.build_tree(preorder, 0, n-1, in_indices)
tree.post_order()

