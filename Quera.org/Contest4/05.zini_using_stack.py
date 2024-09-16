# Problem's Link: https://quera.org/problemset/33023

#       Top, Bottom,        Left, Right
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def count_zini(mat, r, c, visited, n, m):
    stack = [ (r, c) ]
    visited[r][c] = True
    res = 0

    while len(stack)>0:
        r, c = stack[-1]
        stack.pop()

        poss = 0
        for d in DIRS:
            rr, cc = r + d[0], c + d[1]
            if 0 <= rr < n and 0 <= cc < m:
                if not visited[rr][cc]:
                    visited[rr][cc] = True
                    stack.append( (rr,cc) )

                if d[1] == 0:
                    if mat[rr][cc] > mat[r][c]:
                        poss += 1
                    elif mat[rr][cc] < mat[r][c]:
                        poss -= 1
                elif d[0] == 0:
                    if mat[rr][cc] < mat[r][c]:
                        poss += 1
                    elif mat[rr][cc] > mat[r][c]:
                        poss -= 1

        if poss == 4 or poss == -4:
            res += 1
    return res


n, m = map(int, input().split())
numbers = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    numbers.append(list(map(int, input().split())))

print(count_zini(numbers, 0, 0, visited, n, m))
