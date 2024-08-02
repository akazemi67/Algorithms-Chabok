# Problem's Link: https://quera.org/problemset/182271

class BstNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.count_lefts = 0


class BST:
    def __init__(self):
        self.root = None

    def __put(self, node, key):
        if not node:
            return BstNode(key)
        if key <= node.key:
            node.count_lefts += 1
            node.left = self.__put(node.left, key)
        else:
            node.right = self.__put(node.right, key)
        return node

    def put(self, key):
        self.root = self.__put(self.root, key)

    def __rank(self, node, key):
        if not node:
            return 0

        if key <= node.key:
            return self.__rank(node.left, key)
        return 1 + node.count_lefts + self.__rank(node.right, key)

    def rank(self, key):
        return self.__rank(self.root, key)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    i, res = n - 1, 0

    bst = BST()
    while i >= 0:
        res += bst.rank(nums[i])
        bst.put(nums[i])
        i -= 1
    print(res)
