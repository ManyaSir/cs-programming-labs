identificator = str(input())
print("Длина: " + str(len(identificator)))
# print(bool(identificator.isalpha))
print("Только буквы: " + str(identificator.isalpha()))
print("Только цифры: " + str(identificator.isdigit()))
print("Буквенно-цифровая: " + str(identificator.isalnum()))
print("Содержит дефис: "+ str("-" in identificator))





