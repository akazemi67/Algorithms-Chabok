# Problem's Link: https://quera.org/problemset/33023

#       Top, Bottom,        Left, Right
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def count_zini(mat, n, m):
    res = 0 
    for r in range(n):
        for c in range(m):
            
            poss = 0
            for d in DIRS:
                rr, cc = r + d[0], c + d[1]
                if 0 <= rr < n and 0 <= cc < m:
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

print(count_zini(numbers, n, m))
