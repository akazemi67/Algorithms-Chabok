# Problem's Link: https://quera.org/problemset/10327

ns, ok_code = input().split()
n = int(ns)
letters = set(ok_code)

while n > 0:
    code = set(input().strip("\n\t "))
    print("Yes" if code == letters else "No")
    n -= 1
