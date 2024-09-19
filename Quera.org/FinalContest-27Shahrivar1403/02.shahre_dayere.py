# Problem's Link: https://quera.org/problemset/218362

input()
roads = input().split()
hasOne = hasZero = False
for r in roads:
    if r == '1':
        hasOne = True
    else:
        hasZero = True

print("YES" if hasOne and hasZero else "NO")
