# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# теперь надо проверить ее практически
# в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением
# и засекаем общее время выполнения программы
# юзаем библиотеки random и time
# предикаты НЕ ЗАДАЕМ как целое число!
from array import array
import random
from functools import reduce
from datetime import datetime


def check_morgan():
    predicate_number = random.randint(3, 15)
    predicates = array('b', [random.choice([True, False]) for _ in range(predicate_number)])
    print(f"Рандомный предикат: {''.join([str(item) for item in predicates])}", end=" ")

    left_side = not reduce(left_function, predicates)
    right_side = reduce(right_function, predicates[1:], not predicates[0])
    if left_side == right_side:
        print("Утверждение истинно")
    else:
        print("Что-то пошло не так")


def left_function(accumulator, next_element):
    return accumulator or next_element


def right_function(accumulator, next_element):
    return accumulator and not next_element


start_time = datetime.now()

for _ in range(100):
    check_morgan()

print(f"Время выполнения {datetime.now() - start_time}")



