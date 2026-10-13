document_code = input()
category = document_code[0:3]
year = document_code[4:8]
number = document_code[9:13]
inverted_number = number[::-1]
print(f"Категория: {category}")
print(f"Год: {year}")
print(f"Номер: {number}")
print(f"Обратный номер: {inverted_number}")
