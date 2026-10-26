year = int(input())
if not (1 <= year <= 9999):
    print("Ошибка")
    exit()
if ((year % 400) == 0) or (((year % 4) == 0) and ((year % 100) != 0)):
    print("Високосный")
else: print("Невисокосный")
