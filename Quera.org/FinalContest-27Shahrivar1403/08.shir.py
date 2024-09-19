# Problem's Link: https://quera.org/problemset/9723

def check_states(values, caps, states, results):
    if values[0] == 0:
        results.add(values[2])
    if values in states:
        return

    states.add(values)
    for i in range(3):
        if values[i] > 0:
            for j in range(3):
                if i != j:
                    new_values = list(values)
                    val = min(values[i], caps[j] - values[j])
                    new_values[i] -= val
                    new_values[j] += val
                    check_states(tuple(new_values), caps, states, results)


capacities = tuple(map(int, input().split()))

visited_states = set()
results = set()
values = [0] * 3
values[2] = capacities[2]
check_states(tuple(values), capacities, visited_states, results)

for x in sorted(results):
    print(x, end=' ')
