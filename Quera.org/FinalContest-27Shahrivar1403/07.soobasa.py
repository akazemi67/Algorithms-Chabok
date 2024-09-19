# Problem's Link: https://quera.org/problemset/108669

n, a, b = map(int, input().split())
goals = list(map(int, input().split()))

first_half = True
poss = True
for i in range(n):
    if not poss:
        break
    if i < n - 1 and goals[i + 1] == goals[i]:
        poss = False

    if goals[i] > 45 + a:
        first_half = False
    if not first_half:
        if goals[i] > 45 + a and i < n - 1 and goals[i + 1] < goals[i]:
            poss = False
        if goals[i] > 90 + b:
            poss = False

print("YES" if poss else "NO")
