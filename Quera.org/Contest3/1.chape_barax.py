# Problem's Link: https://quera.org/problemset/3405

inp = []
while True:
    s = input()
    if s == "0":
        print('\n'.join(inp[::-1]))
        break
    inp.append(s)

