# Problem's Link: https://quera.org/problemset/335

inp = input().split(',')
stack = []
current_sum = 0

for part in inp:
    value = 0
    for c in part:
        if c == '{':
            stack.append(current_sum)
            stack.append('{')
            current_sum = 0
        elif c == '}':
            current_sum += value
            value = 0

            while stack and stack[-1] != '{':
                current_sum += stack[-1]
                stack.pop()
            stack.pop()
            stack.append(current_sum)

            print(current_sum)
            current_sum = 0
        elif '0' <= c <= '9':
            value = 10 * value + ord(c) - ord('0')

    current_sum += value

