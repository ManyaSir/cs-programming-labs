n = int(input())
if n < 0:
    print("Ошибка")
    exit()
DigitsValue = 0
result = 0
i = 10
if n == 0:
    DigitsValue = 1
else:
    while True:
        if n == 0: break
        result += n % 10
        n = n // 10
        DigitsValue += 1
print("Цифр:", DigitsValue)
print("Сумма цифр:", result)
