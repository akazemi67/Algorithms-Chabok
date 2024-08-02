# Problem's Link: https://quera.org/problemset/182271

def merge(arr, aux, left, mid, right):
    # Copying Array Items
    for i in range(left, right + 1):
        aux[i] = arr[i]

    i, j = left, mid + 1
    cnt = 0
    for k in range(left, right + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > right:
            arr[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1
            cnt += (mid - i + 1)
    return cnt


def merge_sort(arr, aux, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    a = merge_sort(arr, aux, left, mid)
    b = merge_sort(arr, aux, mid + 1, right)
    c = merge(arr, aux, left, mid, right)
    return a + b + c


def count_inversions(arr):
    m = len(arr)
    aux = [0] * m
    return merge_sort(arr, aux, 0, m - 1)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(count_inversions(nums))
