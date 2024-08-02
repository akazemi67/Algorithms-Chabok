# Problem's Link: https://quera.org/problemset/182271

class BinaryIndexedTree:
    def __init__(self, n):
        self.data = [0] * (n + 1)
        self.n = n

    def update(self, idx, val):
        i = idx + 1
        while i <= self.n:
            self.data[i] += val
            i += i & (-i)

    def sum(self, idx):
        res = 0
        i = idx + 1
        while i > 0:
            res += self.data[i]
            i -= i & (-i)
        return res


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    i, res = n - 1, 0

    maxVal = max(nums)
    tree = BinaryIndexedTree(2 * maxVal)

    while i >= 0:
        res += tree.sum(nums[i])
        tree.update(nums[i], 1)
        i -= 1

    print(res)
