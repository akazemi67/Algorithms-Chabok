# Problem's Link: https://quera.org/problemset/237885

def last_pos(places, item):
    if item in places:
        return places[item]
    return -1


def update_diffs(diffs, item, d):
    if item in diffs:
        diffs[item] = max(diffs[item], d)
    else:
        diffs[item] = d


n = int(input())
items = list(map(int, input().split()))
teams_pos = {}
diffs = {}

for i in range(n):
    team = items[i]
    pos = last_pos(teams_pos, team)
    
    d = i+1
    if pos >= 0:
        d = i - pos
    update_diffs(diffs, team, d)
    teams_pos[team] = i

for team in teams_pos:
    update_diffs(diffs, team, n - teams_pos[team])
print(min(diffs.values()))

