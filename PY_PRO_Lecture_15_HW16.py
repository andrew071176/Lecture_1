# 1. Создайте класс «Прямоугольник», у которого присутствуют два поля (ширина и высота).
# Реализуйте метод сравнения прямоугольников по площади. Также реализуйте методы сложения прямоугольников
# (площадь суммарного прямоугольника должна быть равна сумме площадей прямоугольников,
# которые вы складываете). Реализуйте методы умножения прямоугольника на число n (это должно увеличить
# площадь базового прямоугольника в n раз).
import numbers
class Rectangle:
    def __init__(self, h: int | float, w: int | float):
        self.h = h
        self.w = w

    def area(self) -> int | float:
        return self.h * self.w

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.area() + other.area()
        if isinstance(other, int | float):
            return self.area() + other
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return self.area() * other
        else:
            return NotImplemented

    def __str__(self):
        return f'{self.h}x{self.w}'

rect_1 = Rectangle(2, 3)
rect_2 = Rectangle(4, 5)
print(rect_1)
print(rect_2)
print(rect_1.__gt__(rect_2))
print(rect_1.__lt__(rect_2))
print(rect_1.__ge__(rect_2))
print(rect_1.__le__(rect_2))
print(rect_1.__add__(rect_2))
print(rect_1.__mul__(3))
print()

# 2. Создайте класс «Правильная дробь» и реализуйте методы сравнения, сложения, вычитания и произведения
# для экземпляров этого класса.
import math
class Rational:
    def __init__(self, n: int, d: int):
        if not isinstance(n, int):
            raise TypeError('Numerator must be integer number')
        if not isinstance(d, int):
            raise TypeError('Denominator must be integer number')
        if not d:
            raise ZeroDivisionError('Denominator can`t be zero')
        self.n = n
        self.d = d

    def __eq__(self, other):
        k = math.gcd(self.n, self.d)
        self.n //= k
        self.d //= k

        k = math.gcd(other.n, other.d)
        other.n //= k
        other.d //= k
        return (self.n, self.d) == (other.n, other.d)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.n / self.d < other.n / other.d

    def __gt__(self, other):
        return self.n / self.d > other.n / other.d

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        d = self.d * other.d                #calculation common denominator
        n = d // self.d * self.n - \
            d // other.d * other.n          #calculation numerator`s difference
        return Rational(n, d)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        d = self.d * other.d
        n = d // self.d * self.n - \
            d // other.d * other.n
        return Rational(n, d)

    def __isub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        sign = 1 if self.n * self.d > 0 else -1

        d = abs(self.d) * abs(other.d)
        n = d // abs(self.d) * abs(self.n) -\
            d // abs(other.d) * abs(other.n)
        self.n = sign * n
        self.d = d
        return self

    def __str__(self):
        sign = '' if self.n * self.d >= 0 else '-'
        n, d = abs(self.n), abs(self.d)
        k = math.gcd(n, d)
        n //= k
        d //= k

        if n == d:
            return f'{sign}1'
        if d == 1:
            return f'{sign}{n}'
        if n > d:
            return f'{sign}{n // d} {n - n // d * d} / {d}'
        return f'{sign}{n} / {d}'

x1 = Rational(1, 2)
x2 = Rational(3, 4)
print(x1 == x2)     #__eq__
print(x1 != x2)     #__ne__
print(x1 < x2)      #__lt__
print(x1 > x2)      #__gt__
print(x1-x2)        #__sub__
print(x1-x2)        #__rsub__
print(x1-x2)        #__isub__