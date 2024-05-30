items = [3, 5, 10, 12, 17, 21, 25, 28, 33, 36, 40, 44, 47, 50, 56, 64, 68, 70]


def iterative_bin_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def recursive_bin_search(arr, x, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] < x:
        return recursive_bin_search(arr, x, mid + 1, right)
    return recursive_bin_search(arr, x, left, mid - 1)


if __name__ == "__main__":
    # print(recursive_bin_search(items, 44, 0, len(items)-1))
    print(iterative_bin_search(items, 3))
