# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
class Person:
    def __init__(self, id: int):
        self.id = id

    def get_person_data_list(self):
        return self.id

    def __str__(self):
        return f'{self.id}'

# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
class Student(Person):
    def __init__(self, name: str, surname: str, id: int):
        super().__init__(id)
        self.name = name
        self.surname = surname

    def get_student_data_tuple(self) -> list:
        return self.name, self.surname, self.id

    def __str__(self):
        return f'{self.name} {self.surname} ' + super().__str__()

# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
class Group:

    #adding by id
    def add_student(self, student: Student, students_list: list):
        self.student = student
        self.students_list = students_list
        if len(self.students_list) < 10:
            for element in self.students_list:
                if self.student.get_student_data_tuple()[2] ==\
                        element.get_student_data_tuple()[2]:
                    break
            self.students_list.append(student)

    #removal by id
    def removal_student(self, student: Student) -> str:
        self.student = student
        for element in self.students_list:
            if self.student.get_student_data_tuple()[2] ==\
                    element.get_student_data_tuple()[2]:
                self.students_list.remove(element)

    #searching by surname
    def search_student(self, surname: str) -> Student:
        self.surname = surname
        list_students_found = []
        for element in self.students_list:
            if element.get_student_data_tuple()[1] == self.surname:
                list_students_found.append(element)
        return list_students_found


    def __str__(self):
        return f"{'Students list:'}\n{'-'*30}\n" + \
               '\n'.join(map(str, self.students_list)) +'\n'

student_01 = Student('Ivan', 'Ivanov', 1)
student_02 = Student('Petr', 'Ivanov', 2)
student_03 = Student('Sergey', 'Ivanov', 3)
student_04 = Student('Pavel', 'Pavlov', 4)
student_05 = Student('Anton', 'Antonov', 5)
student_06 = Student('Yana', 'Yanovna', 6)
student_07 = Student('Svetlana', 'Svetlova', 7)
student_08 = Student('Yevgeniya', 'Yevgenova', 8)
student_09 = Student('Liubov', 'Liubimova', 9)
student_10 = Student('Liliya', 'Lilova', 10)

students_list = []

group_Python = Group()
group_Python.add_student(student_01, students_list)
group_Python.add_student(student_02, students_list)
group_Python.add_student(student_03, students_list)

print (group_Python)

print (student_01.get_student_data_tuple())

student_001 = Student('Ivan', 'Ivanov', 1)
student_011 = Student('Maksim', 'Ivanov', 11)

print(group_Python.removal_student(student_001))

print(group_Python.search_student('Ivanov'))

print (group_Python)
