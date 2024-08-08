# Problem's Link: https://quera.org/problemset/397


parenthesis = input()

stack = []
result = 0
for p in parenthesis:
    if p == '(':
        stack.append(p)
    else:
        if len(stack) > 0:
            stack.pop()
        else:
            result += 1
            stack.append('(')

result += len(stack)//2
print(result)
