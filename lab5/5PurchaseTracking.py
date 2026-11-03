number = 0
full_cost = 0
medium_cost = 0
while True:
    cost = input()
    if cost == "stop":
        break
    full_cost += int(cost)
    number += 1

if number == 0:
    print("Нет покупок")
else:
    medium_cost = full_cost / number
    print(f"Покупок: {number}\nОбщая стоимость: {full_cost}\nСредняя стоимость: {medium_cost}")
