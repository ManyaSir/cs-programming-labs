temperature_this = input()
temperature_wish = input()
if temperature_this == temperature_wish:
    print("Выключен")
elif float(temperature_this) > float(temperature_wish):
    print("Охлаждение")
elif float(temperature_this) < float(temperature_wish):
    print("Нагрев")
    