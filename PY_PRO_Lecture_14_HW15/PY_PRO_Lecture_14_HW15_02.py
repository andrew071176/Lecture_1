# 1. Рознесіть класи, які використовували під час вирішення завдання про замовлення та
# групу студентів по модулям. Переконайтеся у працездатності проєктів.

# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
import HW15_02_Module_Student
import HW15_02_Module_Group

student_01 = HW_15_02_Module_Student.Student('Ivan', 'Ivanov', 1, 21)
student_02 = HW_15_02_Module_Student.Student('Petr', 'Ivanov', 2, 22)
student_03 = HW_15_02_Module_Student.Student('Sergey', 'Ivanov', 3, 23)
student_04 = HW_15_02_Module_Student.Student('Pavel', 'Pavlov', 4, 24)
student_05 = HW_15_02_Module_Student.Student('Anton', 'Antonov', 5, 25)
student_06 = HW_15_02_Module_Student.Student('Yana', 'Yanovna', 6, 26)
student_07 = HW_15_02_Module_Student.Student('Svetlana', 'Svetlova', 7, 27)
student_08 = HW_15_02_Module_Student.Student('Yevgeniya', 'Yevgenova', 8, 28)
student_09 = HW_15_02_Module_Student.Student('Liubov', 'Liubimova', 9, 29)
student_10 = HW_15_02_Module_Student.Student('Liliya', 'Lilova', 10, 30)

group_Python = HW_15_02_Module_Group.Group('Python')
group_Python.add_student(student_01)
group_Python.add_student(student_02)
group_Python.add_student(student_03)
group_Python.add_student(student_04)
group_Python.add_student(student_05)
group_Python.add_student(student_06)
group_Python.add_student(student_07)
group_Python.add_student(student_08)
group_Python.add_student(student_09)

student_011 = HW_15_02_Module_Student.Student('Maksim', 'Ivanov', 11, 31)
student_001 = HW_15_02_Module_Student.Student('Ivan', 'Ivanov', 1, 21)

# group_Python.add_student(student_011)
group_Python.removal_student(student_001)
print (*group_Python.search_student('Ivanov'))

print (group_Python)