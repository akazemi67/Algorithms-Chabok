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

    def put(self, key):
        if not self.root:
            self.root = BstNode(key)
            return 0

        curr = self.root
        count = 0
        while curr:
            if key <= curr.key:
                curr.count_lefts += 1
                if not curr.left:
                    curr.left = BstNode(key)
                    break
                else:
                    curr = curr.left
            elif key > curr.key:
                count += 1 + curr.count_lefts
                if not curr.right:
                    curr.right = BstNode(key)
                    break
                else:
                    curr = curr.right
        return count


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    i, res = n - 1, 0

    bst = BST()
    while i >= 0:
        res += bst.put(nums[i])
        i -= 1
    print(res)
