# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа.
# Через строку решать нельзя.
from decimal import Decimal

number = Decimal(input("Введите число: "))
while number % 1 > 0:
    number *= 10
number = int(number)

nums = []
while number > 10:
    nums.append(number % 10)
    number //= 10
nums.append(number)
# print(nums)
print(f"Сумма цифр: {sum(nums)}")
