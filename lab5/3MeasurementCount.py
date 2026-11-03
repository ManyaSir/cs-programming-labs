number = int(input())
above_zero = 0
below_zero = 0
equal_zero = 0
for i in range(number):
    temperature = float(input())
    if temperature > 0:
        above_zero += 1
    elif temperature < 0:
        below_zero += 1
    elif temperature == 0:
        equal_zero += 1
print(f"Выше нуля: {above_zero}\nНиже нуля: {below_zero}\nРавны нулю: {equal_zero}")
