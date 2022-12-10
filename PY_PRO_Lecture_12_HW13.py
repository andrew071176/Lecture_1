# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
class Person:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id

    def __str__(self):
        return f'{self.name} {self.surname} {self.id} '

# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
class Student(Person):
    def __init__(self, name: str, surname: str, id: int, age: int):
        super().__init__(name, surname, id)
        self.age = age

    def __str__(self):
        return super().__str__() + f'{self.age} '

# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
class Group:
    def __init__(self, group_title: str, max_students = 10):
        self.group_title = group_title
        self.max_students = max_students

    #adding by id
    def add_student(self, student: Student, students_list: list):
        if len(students_list) < self.max_students:
            for element in students_list:
                if student == element:
                    break
            students_list.append(student)

    #removal by id
    def removal_student(self, student: Student, students_list: list):
        for element in students_list:
            if student.id == element.id:
                students_list.remove(element)

    #searching by surname
    def search_student(self, surname: str, students_list: list) -> Student:
        list_students_found = []
        for element in students_list:
            if element.surname == surname:
                list_students_found.append(element)
        return list_students_found


    def __str__(self):
        return f"\n{'Students list:'}\n{'-'*30}\n" + \
               f"{'Group:'} {self.group_title} \n{'-' * 30}\n" + \
               '\n'.join(map(str, students_list)) +'\n'

student_01 = Student('Ivan', 'Ivanov', 1, 21)
student_02 = Student('Petr', 'Ivanov', 2, 22)
student_03 = Student('Sergey', 'Ivanov', 3, 23)
student_04 = Student('Pavel', 'Pavlov', 4, 24)
student_05 = Student('Anton', 'Antonov', 5, 25)
student_06 = Student('Yana', 'Yanovna', 6, 26)
student_07 = Student('Svetlana', 'Svetlova', 7, 27)
student_08 = Student('Yevgeniya', 'Yevgenova', 8, 28)
student_09 = Student('Liubov', 'Liubimova', 9, 29)
student_10 = Student('Liliya', 'Lilova', 10, 30)

students_list = []

group_Python = Group('Python')
group_Python.add_student(student_01, students_list)
group_Python.add_student(student_02, students_list)
group_Python.add_student(student_03, students_list)
group_Python.add_student(student_04, students_list)
group_Python.add_student(student_05, students_list)
group_Python.add_student(student_06, students_list)
group_Python.add_student(student_07, students_list)
group_Python.add_student(student_08, students_list)
group_Python.add_student(student_09, students_list)


student_011 = Student('Maksim', 'Ivanov', 11, 31)
student_001 = Student('Ivan', 'Ivanov', 1, 21)

group_Python.add_student(student_011, students_list)
group_Python.removal_student(student_001, students_list)
print (*group_Python.search_student('Ivanov', students_list))

print (group_Python)
