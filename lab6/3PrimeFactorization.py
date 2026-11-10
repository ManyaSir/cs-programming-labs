n = int(input())
if n < 2:
    print("Ошибка")
    exit()
result = ""
i = 2
while True:
    if n == 1: break
    if (n % i) == 0:
        result += f"{i} "
        n = n / i
        continue
    else: 
        i += 1
print(result.strip())
