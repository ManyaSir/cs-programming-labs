r, c = [int(i) for i in input().split()]
table = []
row_sum = [0] * r
column_sum = [0] * c
for i in range(r):
    table.append([int(j) for j in input().split()])
for i in range(r):
    for j in range(c):
        row_sum[i] += table[i][j]
for i in range(c):
    for j in range(r):
        column_sum[i] += table[j][i]
print(f"Суммы строк: {row_sum}")
print(f"Суммы столбцов: {column_sum}")
