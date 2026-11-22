r, c = [int(i) for i in input().split()]
table = []
for i in range(r):
    table.append([int(j) for j in input().split()])
IsMatch = False
row_start, row_end, column_start, column_end = [int(i) for i in input().split()]
value = int(input())
for i in range(row_start, row_end + 1):
    for j in range(column_start, column_end + 1):
        if table[i][j] == value:
            print(i, j)
            IsMatch = True
if not IsMatch: print("Не найдено")
