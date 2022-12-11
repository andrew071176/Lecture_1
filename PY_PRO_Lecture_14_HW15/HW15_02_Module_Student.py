import HW15_02_Module_Person

class Student(HW_15_02_Module_Person.Person):
    def __init__(self, name: str, surname: str, id: int, age: int):
        super().__init__(name, surname, id)
        self.age = age

    def __str__(self):
        return super().__str__() + f'{self.age} '