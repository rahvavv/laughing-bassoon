immutable_var = 1, 2, 3, "яблоки", [55, 56, 57]
immutable_var[4][0] = 54  # элинеты списка внутри кортежа изменить можно, другие элименты нет
print("Immutable tuple:", immutable_var)
mutable_list = [1, 2, 3, "яблоки", [55, 56, 57]]
print("Mutable list:", mutable_list)
