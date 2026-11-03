def pascal(n):
    row = [1]

    for i in range(n):
        new_row = [1]

        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])

        new_row.append(1)
        row = new_row

    return " ".join(map(str, row))

def count_odd(n):
    row = [1]
    count = 0

    for i in range(n):
        count += sum(1 for x in row if x % 2 != 0)

        new_row = [1]

        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])

        new_row.append(1)
        row = new_row

    return count
number = int(input())
for i in range(number):
    print(pascal(i))
print(f"Нечётных элементов: {count_odd(number)}")
