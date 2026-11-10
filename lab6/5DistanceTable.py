n = int(input())
if not (1 <= n <= 10):
    print("Ошибка")
    exit()
string = []
for i in range (0, n):
    for j in range (0, n):
        string.append(str(abs(j - i)))
    print(" ".join(string))
    string = []
    