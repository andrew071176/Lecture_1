import HW15_02_Module_Student

class Group:
    def __init__(self, group_title: str, max_students = 10):
        self.group_title = group_title
        self.max_students = max_students
        self.students_list = []

    # adding_by_id
    def add_student(self, student: HW_15_02_Module_Student.Student):
        if not isinstance(student, HW_15_02_Module_Student.Student):
            raise TypeError('The student isn`t instance of class Student')
        if len(self.students_list) >= self.max_students:
            raise ValueError('The list of students cannot be extended as it is fully formed')
        else:
            for element in self.students_list:
                if student.id == element.id:
                    break
            self.students_list.append(student)

    #removal by id
    def removal_student(self, student: HW_15_02_Module_Student.Student):
        for element in self.students_list:
            if student.id == element.id:
                self.students_list.remove(element)

    #searching by surname
    def search_student(self, surname: str) -> list:
        list_students_found = []
        for element in self.students_list:
            if element.surname == surname:
                list_students_found.append(element)
        return list_students_found

    def __str__(self):
        return f"\n{'Students list:'}\n{'-'*30}\n" + \
               f"{'Group:'} {self.group_title} \n{'-' * 30}\n" + \
               '\n'.join(map(str, self.students_list)) +'\n'