# 1. Создайте декоратор, который будет подсчитывать, сколько раз была вызвана
# декорируемая функция.
def counter_f(f: 'function') -> int:
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        if f(*args, **kwargs) or not f(*args, **kwargs):
            counter += 1
        return counter
    return wrapper

@counter_f
def sum(x: int, y: int) -> int:
    return x + y

print ([sum (i, i) for i in range (10)][-1])

# 2. Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций, для обработки
# последовательности.
def register_f(f: 'function', ff_list: list = []) -> list:
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        if f not in ff_list:
            ff_list.append(f)
        return ff_list
    return wrapper

@register_f
def sum(x: int, y: int) -> int:
    return x + y

@register_f
def sub(x: int, y: int) -> int:
    return x - y

print (sum(1, 2))
print (sum(3, 4))
print (sub(5, 6))
print (sub(7, 8))

# 3. Предположим, в классе определен метод __str__, который возвращает строку на основании класса.
# Создайте такой декоратор для этого метода, чтобы полученная строка сохранялась в текстовый файл,
# имя которого совпадает с именем класса, метод которого вы декорировали.
def Decorator_load_str_to_text_file(method: 'method') -> 'file':
    def wrapper(*args):
        file_name = method.__str__()[10:-31]
        with open(f'{file_name}.txt', 'w') as f:
            return f.write(method(*args))
    return wrapper

class ABC:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @Decorator_load_str_to_text_file
    def __str__(self):
        return f'{self.x + self.y}'

a = ABC(10, 10)
a.__str__()

# 4. Создайте декоратор с параметрами для проведения хронометража работы той или иной функции.
# Параметрами должны выступать то, сколько раз нужно запустить декорируемую функцию и в какой файл
# сохранить результаты хронометража. Цель - провести хронометраж декорируемой функции.
import time
def decorator_timer_f(function: 'function', file_name: str = 'chrono_result.txt', counter: int = 10) -> int:
    def wrapper(*args, **kwargs):
        total_time = 0
        for _ in range (counter):
            start_time = time.perf_counter()
            x = function(*args, **kwargs)
            stop_time = time.perf_counter()
            total_time += (stop_time - start_time)
        with open(file_name, 'w') as f:
            f.write(f'{total_time/counter:.10f}')
            return x
    return wrapper

@decorator_timer_f
def sum(x, y):
    return x + y

sum(10, 2)

# 5. Создайте декоратор, который зарегистрирует декорируемый класс в списке классов.
def register_class(cls, classes_list: list = []) -> list:
    def wrapper():
        if cls not in classes_list:
            classes_list.append(cls)
        return classes_list
    return wrapper

@register_class
class A:
    pass
@register_class
class B:
    pass

print (A())
print (B())

# 6. Создайте декоратор класса с параметром. Параметром должна быть строка, которая должна дописываться
# (слева) к результату работы метода __str__.
def add_left(cls, left_str: str = '***') -> str:
    def wrapper(*args, **kwargs):
        return f'{left_str}{cls(*args, **kwargs)}'
    return wrapper

@add_left
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}x{self.y}x{self.z}'

print (Box(1, 2, 3))

# 7. Для класса Box напишите статический метод, который будет подсчитывать суммарный объем двух ящиков,
# которые будут его параметрами.
class Box:
    def __init__(self, box_1, box_2):
        self.box_1 = box_1
        self.box_2 = box_2
        self.boxes_volume = self.calc_boxes_volume(box_1, box_2)

    @staticmethod
    def calc_boxes_volume(box_1, box_2):
        return box_1 + box_2

    def __str__(self):
        return f'{self.box_1} * {self.box_2}'

a = Box(5, 10)
print(a.boxes_volume)
print(a.calc_boxes_volume(20, 30))

