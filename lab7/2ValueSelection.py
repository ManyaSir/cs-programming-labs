numbers = [int(i) for i in input().split()]
squared_numbers = [number ** 2 for number in numbers if (number > 0 and number % 2 == 1)]
print(f"Квадраты: {squared_numbers}")
