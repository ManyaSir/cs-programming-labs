numbers = [int(i) for i in input().split()]
number = int(input())
indexes = []
for index, value in enumerate(numbers):
    if value == number:
        indexes.append(index)
print(f"Индексы: {indexes}")
