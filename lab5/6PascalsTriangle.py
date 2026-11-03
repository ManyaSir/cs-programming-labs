count_odd = 0
def pascalString(n):
    result = ""
    for k in range(0, n + 1):
        result = result + " " + str(numberOfString(n, k))
    return result.lstrip()
def numberOfString(n,k):
    global count_odd
    result = factorial(n) / (factorial(k) * factorial(n - k))
    if (int(result) % 2) != 0: count_odd += 1
    return int(result)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    if n == 0: result = 1
    return result
number = int(input())
for i in range (number):
    print(pascalString(i))
print(f"Нечётных чисел: {count_odd}")



