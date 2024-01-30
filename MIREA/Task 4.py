n, m = map(int, input().split())
p = [list(map(int, input().split())) for i in range(n)]
a = [[0] * m for i in range(n)]
b = [[''] * m for i in range(n)]
a[0][0] = p[0][0]
for j in range(1, m):
    a[0][j] = a[0][j - 1] + p[0][j]
    b[0][j] = b[0][j - 1] + 'R '
for i in range(1, n):
    a[i][0] = a[i - 1][0] + p[i][0]
    b[i][0] = b[i - 1][0] + 'D '
for i in range(1, n):
    for j in range(1, m):
        if a[i][j - 1] > a[i - 1][j]:
            a[i][j] = a[i][j - 1] + p[i][j]
            b[i][j] = b[i][j - 1] + 'R '
        else:
            a[i][j] = a[i - 1][j] + p[i][j]
            b[i][j] = b[i - 1][j] + 'D '
print(a[-1][-1])
print(b[-1][-1])
