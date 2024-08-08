# Problem's Link: https://quera.org/problemset/3538


def day_index(day):
    if day[0] == 's':
        return 0
    if day[0] == 'j':
        return 6
    return int(day[0])


days = set()
for _ in range(3):
    input()
    week_days = input().split()
    for day in week_days:
        days.add(day_index(day))

print(7-len(days))
