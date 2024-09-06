def floyd_warshal(mat, n):
    for k in range(1, n + 1):
        for u in range(1, n + 1):
            for v in range(1, n + 1):
                mat[u][v] = min(mat[u][k] + mat[k][v], mat[u][v])


n = 5
mat = [[10 ** 5] * (n + 1) for _ in range(n + 1)]
mat[1][2] = 1
mat[1][3] = 5
mat[1][4] = 7
mat[2][3] = 2
mat[2][5] = 2
mat[3][4] = 1
mat[4][2] = 4
mat[5][1] = 3
floyd_warshal(mat, 5)
for x in mat:
    print(x)
