# Задача 3. Разделители символов
# Человек хочет сделать рассылку поздравлений для определённого списка людей. Поздравления для разных людей он хочет написать по-разному.
#
# Напишите программу, которая запрашивает у пользователя:
# Шаблон поздравления (туда вставляется ФИ и возраст)
# ФИ людей (в одну строку, разделяются запятой)
# Возраст каждого человека (в одну строку через пробел)
# В конце  программа выводит поздравления и всех именинников в одну строку вместе с их возрастом.
#
# Пример:
# Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: С днём рождения, {name}! С {age}-летием тебя!
# Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова
# Возраст людей через пробел: 20 30 18
#
# С днём рождения, Иван Иванов! С 20-летием тебя!
# С днём рождения, Петя Петров! С 30-летием тебя!
# С днём рождения, Лена Ленова! С 18-летием тебя!
#
# Именинники: Иван Иванов 20, Петя Петров 30, Лена Ленова 18

while True:
    user_input = input('Введите шаблон поздравления, в шаблоне необходимо использовать конструкцию {name} и {age}: ')
    if '{name}' in user_input and '{age}' in user_input:
        break
    print('Ошибка! Отсутствует одна или две конструкции!')
name_list = input('Список людей через запятую: ').split(', ')
age_str = input('Возраст людей через пробел: ')
age = [int(i_number) for i_number in age_str.split()]

for i_man in range(len(name_list)):
    print(user_input.format(name=name_list[i_man], age=age[i_man]))

people = [
    ' '.join([name_list[i_man], str(age[i_man])])
    for i_man in range(len(name_list))
]

people_str = ', '.join(people)

print('Именинники:', people_str)
