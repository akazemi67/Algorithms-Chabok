# Problem's Link: https://quera.org/problemset/3412

persons = []
for _ in range(4):
    per, pos = input().split()
    if pos=='L':
        persons.insert(0, per)
    elif pos=='R':
        persons.append(per)

print(persons[1])

