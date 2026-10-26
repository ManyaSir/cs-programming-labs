ticket_cost = float(input())
if ticket_cost <=0:
    print("Ошибка")
    exit()
age = int(input())
if not (0 < age <= 120):
    print("Ошибка")
    exit()
elif (0 < age <= 5):
    print(f"Стоимость: 0 руб")
elif (6 <= age <= 17):
    cost = ticket_cost * 0.5
    print(f"Стоимость: {cost:.2f} руб")
elif (18 <= age <= 59):
    cost = ticket_cost
    print(f"Стоимость: {cost:.2f} руб")
elif (60 <= age <= 120):
    cost = ticket_cost * 0.7
    print(f"Стоимость: {cost:.2f} руб")
    