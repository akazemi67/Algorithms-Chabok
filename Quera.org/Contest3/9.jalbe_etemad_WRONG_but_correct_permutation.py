# Problem's Link: https://quera.org/problemset/69902

def merge(arr, left, mid, right, data):
    global idx
    aux = arr[::]

    i, j = left, mid + 1
    for k in range(left, right + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > right:
            arr[k] = aux[i]
            i += 1
        elif idx < len(data) and data[idx]=='1':
            arr[k] = aux[i]
            i += 1
            idx += 1
        else:
            arr[k] = aux[j]
            j += 1
            idx += 1


def merge_sort(arr, left, right, data):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid, data)
    merge_sort(arr, mid + 1, right, data)
    merge(arr, left, mid, right, data)


def checksum(arr):
    result = 1
    for a in arr:
        result = (31 * result + a) % 1000003
    return result


n = int(input())
data = input()

idx = 0
arr = [i for i in range(n)]
merge_sort(arr, 0, n-1, data)
ans = [0]*n
for i in range(n):
    ans[arr[i]] = i+1

print(checksum(ans))

