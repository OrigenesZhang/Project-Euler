f = open('11.in', 'r')
mat = []

for i in range(20):
    now = list(map(int, f.readline().split()))
    mat.append(now)

ans = 0

for i in range(20):
    for j in range(20):
        if j + 4 > 20:
            break
        now = 1
        for k in range(j, j + 4):
            now *= mat[i][k]
        ans = max(ans, now)
        now = 1
        for k in range(j, j + 4):
            now *= mat[k][i]
        ans = max(ans, now)

for i in range(20):
    for j in range(20):
        if j + 4 > 20:
            break
        now = 1
        if i + j + 3 < 20:
            for k in range(4):
                now *= mat[j + k][i + j + k]
            ans = max(ans, now)
            now = 1
            for k in range(4):
                now *= mat[i + j + k][j + k]
            ans = max(ans, now)
        now = 1
        if i + j - 3 >= 0 and i + j < 20:
            for k in range(4):
                now *= mat[j + k][i + j - k]
            ans = max(ans, now)
            now = 1
            for k in range(4):
                now *= mat[i + j - k][j + k]
            ans = max(ans, now)
print(ans)

