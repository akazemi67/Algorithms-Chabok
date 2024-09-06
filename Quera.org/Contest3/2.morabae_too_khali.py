# Problem's Link: https://quera.org/problemset/283

a = int(input())
b = int(input())

if a<=b:
    print("Wrong order!")
    exit(0)
if (a-b)%2 == 1:
    print("Wrong difference!")
    exit(0)

lines = (a-b)//2
for _ in range(lines):
    print("* "*a)

for _ in range(b):
    print("* "*lines, end='')
    print(" "*(2*b), end='')
    print("* "*lines)

for _ in range(lines):
    print("* "*a)

