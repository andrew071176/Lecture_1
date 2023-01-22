# 1. Создайте дескриптор, который будет делать поля класса управляемые им доступными только
# для чтения.
class Descriptor_read_only:
    def __init__(self, attr_name):
        self.attr = attr_name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.attr)

    def __set__(self, instance, value):
        if self.attr not in instance.__dict__:
            instance.__dict__[self.attr] = value
        else:
            raise AttributeError('field is read-only')

class A:
    def __init__ (self, a, b, field = '10'):
        self.a = a
        self.b = b
        self.field = field
    field = Descriptor_read_only('field')

    def __str__(self):
        return f'{self.a} {self.b} {self.field}'

a1 = A(1, 2)
a2 = A(3, 4, 100)
print(a1.field)
print(a2.field)
a1.field = 1000

# 2. Реализуйте функционал, который будет запрещать установку полей класса любыми значениями, кроме целых
# чисел. Т.е., если тому или иному полю попытаться присвоить, например, строку, то должно быть возбужденно
# исключение.
class Persons:
    def __init__(self, man: int = 1, woman: int = 1):
        self.man = man
        self.woman = woman

    def __str__(self):
        return 'Persons [man = '+str(self.man)+', woman = '+str(self.woman)+']'

    def __setattr__(self, attr_name, attr_value):
        if not isinstance(attr_value, int):
            raise AttributeError ('field is int-only')
        else:
            self.__dict__[attr_name] = attr_value

persons_1 = Persons(1, 2.5)

# 3. Реализуйте свойство класса, которое обладает следующим функционалом: при установки значения этого
# свойства в файл с заранее определенным названием должно сохранятся время (когда устанавливали значение
# свойства) и установленное значение.
import datetime
class A:
    def __init__(self, __a1, a2):
        self.__a1 = __a1
        self.a2 = a2

    def get_a1(self):
        print ('call get a1')
        return self.__a1

    def set_a1(self, a1_value):
        with open ('set_timing.txt', 'a') as f:
            f.write(f'{datetime.datetime.now()}***{a1_value}\n')
        print ('call set_a1')
        self.__a1 = a1_value

    a1 = property(get_a1, set_a1, 'a1_value')

    def __str__(self):
        return 'A [a1 = '+str(self.__a1)+', a2 = '+str(self.a2)+']'

A1 = A(1, 2)
A1.a1 = 10

# 4. Реализуйте метакласс, который обладает следующим функционалом: при его использовании в файл с заранее
# определенным названием нужно сохранить имя класса и список его полей.
class MetaClass(type):
    def __new__(typeclass, classname, supers, classdict):
        return type.__new__(typeclass, classname, supers, classdict)
    def __init__(typeclass, classname, supers, classdict):
        with open('metaone.txt', 'w') as f:
                f.write(f'{classname} {classdict}')

class ABC (metaclass = MetaClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 5. Создайте ABC класс с абстрактным методом проверки целого числа на простоту. Т.е., если параметром этого
# метода является целое число и оно простое, то метод должен вернуть True, а в противном случае False.
import abc
class IntegerPrimeValidator(abc.ABC):
    @abc.abstractmethod
    def integer_prime_validate(self, value):
        "Validate integer prime number"

class NumberValidator(IntegerPrimeValidator):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def integer_prime_validate(self, value):
        if isinstance(value, int):
            print(value)
            for i in range(2, (value // 2) + 1):
                if value % i == 0:
                    return False
            return True
        else:
            return False

a = NumberValidator(4)
print(a)
print(a.integer_prime_validate(13))
print(a)

# 6. Создайте класс его наследующий.
import abc
class A(abc.ABC):
    pass

class AA(A):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'{text}'

# 7. Создайте класс, который не наследует пользовательский ABC класс, но обладает нужным методом.
# Зарегистрируйте его в качестве виртуального подкласса.
import abc
class A(abc.ABC):
    pass

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 8. Проверьте работоспособность проекта.
A.register(Rectangle)
box_1 = Rectangle(1, 2)
print(isinstance(box_1, A))
