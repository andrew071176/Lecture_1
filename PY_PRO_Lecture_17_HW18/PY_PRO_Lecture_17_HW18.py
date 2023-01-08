# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної
# прогресії із зазначеним множником.
#  Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі
#  команди на завершення.
def geometrical_progression(multiplier: int, num: int = 2, limit: int = 200) -> int:
    product = multiplier * num
    while product <= limit:     #reaching a certain value
        yield product
        num = product
        product = multiplier * num
    return

g = geometrical_progression(2, 2)
for _ in range (5):
    if next(g) > 200:
        g.close()             #sending command to end
    print (next(g))

# 2. Реалізуйте свій аналог генераторної функції range().
def my_range(start: int, stop = None, step = None):
    if not stop:
        stop = start
        start = 0
    if not step:
        step = 1
    next_step = start
    while next_step <= stop:
        yield next_step
        start = next_step
        next_step = start + step
    return

g = my_range(-1, 5, 2)
print (next(g))
print (next(g))
print (next(g))
print (next(g))

# 3. Напишіть функцію-генератор, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана
# параметром цієї функції.
def prime_num (limit: int):
    for num in range (2, limit + 1):
        divider = 2
        while divider < num:
            if not num % divider:
                break
            divider += 1
        else:
            yield num
    return

g = prime_num(5)
print (next(g))
print (next(g))
print (next(g))

# 4. Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел
# від 2 до вказаної вами величини.
list_degree_3 = (num**3 for num in range (2, 10))
print (*list_degree_3)
