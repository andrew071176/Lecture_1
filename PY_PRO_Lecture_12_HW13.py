# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
class Person:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id

    def get_person_data_list(self):
        return [self.name, self.surname, self.id]

    def __str__(self):
        return f'{self.name} {self.surname} {self.id}'

# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
class Student(Person):
    def __init__(self, name: str, surname: str, id: int, group: str):
        super().__init__(name, surname, id)
        self.group = group

    def get_student_data_list(self) -> list:
        return [self.name, self.surname, self.id, self.group]

    def __str__(self):
        return super().__str__() + f' {self.group}'

# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
class Group:
    def __init__(self):
        student_01 = Student('Ivan', 'Ivanov', 1, 'Python')
        student_02 = Student('Petr', 'Ivanov', 2, 'Python')
        student_03 = Student('Sergey', 'Ivanov', 3, 'Python')
        student_04 = Student('Pavel', 'Pavlov', 4, 'Python')
        student_05 = Student('Anton', 'Antonov', 5, 'Python')
        student_06 = Student('Yana', 'Yanovna', 6, 'Java')
        student_07 = Student('Svetlana', 'Svetlova', 7, 'Java')
        student_08 = Student('Yevgeniya', 'Yevgenova', 8, 'Java')
        student_09 = Student('Liubov', 'Liubimova', 9, 'Java')
        student_10 = Student('Liliya', 'Lilova', 10, 'Java')

        self.students_list = [student_01, student_02, student_03, student_04, student_05,
                              student_06, student_07, student_08, student_09, student_10]

    #adding by id
    def add_student(self, student: Student) -> str:
        self.student = student
        if len(self.students_list) < 10:
            for element in self.students_list:
                if self.student.get_student_data_list()[2] ==\
                        element.get_student_data_list()[2]:
                    return f"{'Student ('}"\
                           f"{' '.join(map(str, (self.student.get_student_data_list())))}" \
                           f"{') is already enrolled'}\n"
            self.students_list.append(student)
            return f"{'Student ('}" \
                   f"{' '.join(map(str, (self.student.get_student_data_list())))}" \
                   f"{') is successfully enrolled'}\n"
        else:
            return f"{'Student ('}" \
                   f"{' '.join(map(str, (self.student.get_student_data_list())))}" \
                   f"{') can`t be enrolled into list because list is fully enrolled'}\n"

    #removal by id
    def removal_student(self, student: Student) -> str:
        self.student = student
        for element in self.students_list:
            if self.student.get_student_data_list()[2] ==\
                    element.get_student_data_list()[2]:
                self.students_list.remove(element)
                return f"{'Student ('}"\
                       f"{' '.join(map(str, (self.student.get_student_data_list())))}" \
                       f"{') is successfully removed'}\n"
            else:
                return f"{'Student ('}"\
                       f"{' '.join(map(str, (self.student.get_student_data_list())))}" \
                       f"{') isn`t removed (not found)'}\n"

    #searching by surname
    def search_student(self, surname: str) -> str:
        self.surname = surname
        found_students = ''
        for element in self.students_list:
            if element.get_student_data_list()[1] == self.surname:
                found_students += f"{' '.join(map(str, (element.get_student_data_list())))}\n"
        if len (found_students) > 0:
            return f"{'Student(s) with surname '}"\
                   f"{self.student.get_student_data_list()[1]}"\
                   f"{' found in list:'}\n"\
                   f"{found_students}\n"
        else:
            return f"{'Student(s) with surname '}"\
                   f"{self.student.get_student_data_list()[1]}"\
                   f"{' isn`t found in list:'}"\
                   f"{found_students}\n"

    def __str__(self):
        return f"{'Students list:'}\n{'-'*30}\n" + \
               '\n'.join(map(str, self.students_list)) +'\n'

student_1 = Student('Ivan', 'Ivanov', 1, 'Python')
student_11 = Student('Maksim', 'Ivanov', 11, 'C++')

group_1 = Group()
print(group_1.add_student(student_1))
print(group_1.removal_student(student_1))
print(group_1.add_student(student_11))
print(group_1.search_student('Ivanov'))
print (group_1)
