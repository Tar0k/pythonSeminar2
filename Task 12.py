# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import random

x = random.randint(1, 1000)
y = random.randint(1, 1000)

print(x, y)
known_sum = x + y
known_product = x * y

for arg1 in range(1, known_sum):
    arg2 = known_sum - arg1
    if arg1 * arg2 == known_product:
        print(f"Загаданные значения: {arg1}, {arg2}")
        break
