# Problem's Link: https://quera.org/problemset/69899

n, k = map(int, input().split())
players = []
for i in range(1, n + 1):
    players.extend([i, i])

it = 0
while len(players) > 1:
    t = k
    L = len(players)

    while t > 0:
        print(players[it], end=' ')
        t -= 1
        it = (it + 1) % L
    print()

    it = (it - 1 + L) % L
    del players[it]
    if it == L-1:
        it = 0

    if len(players) == 2 and players[0] == players[1]:
        break

print(f"winner:{players[0]}")

