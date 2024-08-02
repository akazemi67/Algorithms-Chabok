# Problem's Link: https://quera.org/problemset/3558

def read_numbers():
    a, b = input().split()
    return int(a), int(b)


def add(nums, ran):
    for a in range(ran[0], ran[1] + 1):
        nums.add(a)


n, m = read_numbers()
one = set()
two = set()
for _ in range(n):
    add(one, read_numbers())
for _ in range(m):
    add(two, read_numbers())

print(len(one.intersection(two)))
