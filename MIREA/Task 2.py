a = [list(range(i, i + 8) if i % 16 else reversed(range(i, i + 8))) for i in range(0, 63, 8)]
b = zip(*[list(reversed(i)) for i in a])
c = [[0] * 8 for _ in range(8)]
val = -1
for k in range(8 + 8):
    tmp = min(k, max(8 - 1, 8 - 1))
    for j in range(tmp, -1, -1):
        if k % 2:
            row = k - j
            col = j
        else:
            row = j
            col = k - j
        if row < 8 and col < 8:
            val += 1
            c[row][col] = val

[print('\t'.join([str(el) for el in i])) for i in b]
print()
[print('\t'.join([str(el) for el in i])) for i in a]
print()
[print('\t'.join([str(el) for el in i])) for i in c]
