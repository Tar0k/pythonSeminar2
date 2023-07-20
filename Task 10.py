# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монеток на столе: "))
# Вычисляем возможные комбинации, где двоичные числа представляют, выпавшие монетки
# 0 - решка
# 1 - герб
combinations = {f"{{:0>{n}b}}".format(value): f"{{:0>{n}b}}".format(value).count("0") for value in range(pow(2, n))}


def eagle_tail(combination):
    return ", ".join(["герб" if item == '1' else "решка" for item in combination])


print("Для следующих комбинаций необходимое минимальное количество переворотов")
# [print(f"{key}: {value if value != 0 else 'не требуется'}") for key, value in combinations.items()]
[print(f"{eagle_tail(key)}: {value if value != 0 else 'не требуется'}") for key, value in combinations.items()]
