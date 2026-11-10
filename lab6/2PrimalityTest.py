n = int(input())
if n < 2:
    print("Не простое")
    exit()
i = 2
while i ** 2 <= n:
    if (n % i) == 0:
        print("Не простое")
        exit()
    else: 
        i += 1
print("Простое")
