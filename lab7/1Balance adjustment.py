goods = [int(i) for i in input().split()]
inverted_goods = goods.copy()
for i in inverted_goods:
    if i < 0:
        inverted_goods[inverted_goods.index(i)] = 0
print(f"Исходные остатки: {goods}")
print(f"Исправленные остатки: {inverted_goods}")
