# Problem's Link: https://quera.org/problemset/291

def check_substr(strings, ss):
    for i in range(1, len(strings)):
        if not (ss in strings[i] or ss in strings[i][::-1]):
            return False
    return True


n = int(input())
substrs = []
for _ in range(n):
    substrs.append(input())


L = len(substrs[0])
maxLen = 0
result = ""
for i in range(L):
    for j in range(i, L):
        ss = substrs[0][i:j+1]
        if check_substr(substrs, ss) and len(ss) > maxLen:
            maxLen = len(ss)
            result = ss

print(result)

