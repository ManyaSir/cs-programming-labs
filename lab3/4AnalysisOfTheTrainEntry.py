info = input()
number, d_from, d_to, time, cost = info.split(";")
print(f"Поезд: {number}\nМаршрут: {d_from} - {d_to}\nОтправление: {time}\nЦена: {float(cost):.2f}")
