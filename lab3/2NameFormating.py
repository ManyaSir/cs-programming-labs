full_name = input()
surname, given_name, middle_name = full_name.split()
print(f"{surname.capitalize()} {given_name[0].capitalize()}. {middle_name[0].capitalize()}.")
