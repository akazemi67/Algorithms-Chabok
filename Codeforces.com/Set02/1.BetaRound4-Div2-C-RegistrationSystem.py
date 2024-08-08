# Problem's Link: https://codeforces.com/problemset/problem/4/C

names = {}

t = int(input())
while t>0:
    name = input()
    if name not in names:
        print("OK")
        names[name] = 1
    else:
        print(f"{name}{names[name]}")
        names[name] += 1
    t -= 1
    
   