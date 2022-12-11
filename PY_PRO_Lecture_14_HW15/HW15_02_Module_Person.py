class Person:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id

    def __str__(self):
        return f'{self.name} {self.surname} {self.id} '