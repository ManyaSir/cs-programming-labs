a = int(input())
b = int(input())
c = 0
if (a < 0) or (b < 0) or ((a == 0) and (b == 0)):
    print("Ошибка")
    exit()
while True:
    if (a % b) == 0:
        print("НОД:", b)
        break
    c = a
    a = b
    b = c % b

    