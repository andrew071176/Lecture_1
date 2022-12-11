class Buyer:
    def __init__(self, name, surname, mobile_phone):
        self.name = name
        self.surname = surname
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f'{self.name} {self.surname} {self.mobile_phone}'