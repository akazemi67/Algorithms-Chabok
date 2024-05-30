import random


def merge(arr, left, mid, right):
    # Copying Array Items
    aux = arr[::]

    i, j = left, mid + 1
    for k in range(left, right + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > right:
            arr[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


if __name__ == "__main__":
    items = [random.randint(1, 1000) for _ in range(10)]
    print(f"Items = {items}")
    merge_sort(items, 0, len(items) - 1)
    print(f"Sorted Items = {items}")
