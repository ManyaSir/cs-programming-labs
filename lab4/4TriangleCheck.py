a = int(input())
b = int(input())
c = int(input())
if ((a + b) <= c) or ((a + c) <= b) or ((b + c) <= a):
    print("Треугольник не существует")
elif a == b == c:
    print("Треугольник равносторонний")
elif (a == b) or (a == c) or (b == c):
    print("Треугольник равнобедренный")
else: print("Разносторонний")
