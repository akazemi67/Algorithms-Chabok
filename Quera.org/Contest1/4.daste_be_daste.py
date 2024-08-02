# Problem's Link: https://quera.org/problemset/3433

def calc(powers, l, r):
    if l == r:
        return powers[l]

    mid = (l + r) // 2
    left_val = calc(powers, l, mid)
    right_val = calc(powers, mid + 1, r)

    if left_val > right_val:
        return left_val + max(powers[mid + 1:r + 1])
    return right_val + max(powers[l:mid + 1])


n = int(input())
teams = 2 ** n
powers = list(map(int, input().split()))
print(calc(powers, 0, teams - 1))
