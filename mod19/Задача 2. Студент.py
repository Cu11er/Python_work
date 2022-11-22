# Пользователь вводит фамилию, имя студента, город проживания, вуз, в котором он учится, и все его оценки.
# Всё вводится в одну строку через пробел. Напишите программу, которая по этой информации составит словарь и выведет его на экран.
#
# Пример:
# Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): Илья Иванов Москва МГУ 5 4 4 4 5
#
# Результат:
# Имя - Илья
# Фамилия - Иванов
# Город - Москва
# Место учёбы - МГУ
# Оценки - [5, 4, 4, 4, 5]

student = input(
    'Введите информацию о студенте через пробел\n'
    '(имя, фамилия, город, место учебы, оценки): '
)

student_list = student.split()

student_dict = dict()

for i_list in student_list:
    student_dict['Имя'] = student_list[0]
    student_dict['Фамилия'] = student_list[1]
    student_dict['Город'] = student_list[2]
    student_dict['Место учебы'] = student_list[3]
    student_dict['Оценки'] = []
for i_grade in student_list[4:]:
    student_dict['Оценки'].append(int(i_grade))

for i_info in student_dict:
    print(i_info, '-', student_dict[i_info])
