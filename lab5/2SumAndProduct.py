a = int(input())
b = int(input())
sum = 0
product = 1
for i in range(a, b + 1):
    sum += i
for i in range(a, b + 1):
    product *= i
print(f"Сумма: {sum}\nПроизведение: {product}")
