phone_number = input()
phone_number = phone_number.strip().replace("+", "").replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
print(phone_number)
