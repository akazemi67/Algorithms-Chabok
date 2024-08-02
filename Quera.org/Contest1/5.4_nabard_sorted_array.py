# Problem's Link: https://quera.org/problemset/182271

def index(arr, value):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] <= value:
            l = m + 1
        else:
            r = m - 1
    return l


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    i, res = n - 1, 0

    items = []
    while i >= 0:
        idx = index(items, nums[i])
        res += idx
        items.insert(idx, nums[i])
        i -= 1
    print(res)
