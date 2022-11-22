# Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год сохранены в словаре в виде пар «название фрукта — доход»:
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода.
# Напишите программу, которая находит общий доход, затем выводит фрукт с минимальным доходом и удаляет его из словаря. Выведите итоговый словарь на экран.
# Результат работы программы:
# Общий доход за год составил 35419.34 рублей
# Самый маленький доход у grapefruit. Он составляет 300.4 рублей
# Итоговый словарь: {'apple': 5600.2, 'orange': 3500.45, 'banana': 5000.0, 'bergamot': 3700.56, 'durian': 5987.23, 'peach': 10000.5, 'pear': 1020.0, 'persimmon': 310.0}

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

min_value = min(incomes.values())
min_key = ''
for val in incomes:
    if incomes[val] == min_value:
        min_key = val

print('Оющий доход за год составил', sum(incomes.values()), 'рублей')
incomes.pop(min_key)
print('Самый маленький доход у', min_key, '. Он составляет', min_value, 'рублей')
print('Итоговый словарь:', incomes)
