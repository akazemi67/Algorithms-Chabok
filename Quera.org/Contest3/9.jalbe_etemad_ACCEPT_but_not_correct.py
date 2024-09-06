# Problem's Link: https://quera.org/problemset/69902


def merge(L, R, data):
    global idx
    res = []

    n, m = len(L), len(R)
    i, j = 0, 0
    while i<n and j<m:
        if idx < len(data) and data[idx]=='1':
            res.append(L[i])
            i += 1
            idx += 1
        else:
            res.append(R[j])
            j += 1
            idx += 1

    res.extend(L[i:])
    res.extend(R[j:])
    return res


def merge_sort(left, right, data):
    if right - left == 1:
        return [left]

    mid = (left + right) // 2
    L = merge_sort(left, mid, data)
    R = merge_sort(mid, right, data)
    return merge(L, R, data)

def checksum(arr):
    result = 1
    for a in arr:
        result = (31 * result + a) % 1000003
    return result


n = int(input())
data = input()

idx = 0
arr = merge_sort(0, n, data)
ans = [0]*n
for i in range(n):
    ans[arr[i]] = i+1

print(checksum(ans))



