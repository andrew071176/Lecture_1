# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
# закон якої задається за допомогою функції користувача.
#  Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та
#  кількість членів, що видаються послідовностю.
#  Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди
#  на завершення.
def users_f(item):
    return item**2

def gen_f (start: int = 1, counter: int = 1, users_f: object = None) -> int:
    iter = 1
    while iter < counter:
        yield users_f(start)
        start += 1
        iter += 1
    return

for value in gen_f (1, 10, users_f):
    print (value)

# 2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація -
# https://en.wikipedia.org/wiki/Memoization .
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду
# Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.
# Standard
def fibonacci(number: int = 2) -> int:
    first_number = 0
    second_number = 1
    def get_next():
        nonlocal number
        nonlocal second_number
        nonlocal first_number
        if number == 1:
            return first_number
        elif number == 2:
            return second_number
        else:
            for _ in range (2, number):
                next_number = second_number + first_number
                first_number = second_number
                second_number = next_number
            return next_number
    return get_next

# #Memoization
def fibonacci_memo(fibonacci_list, number: int = 2) -> int:
    first_number = 0
    second_number = 1
    def get_next():
        nonlocal number
        nonlocal second_number
        nonlocal first_number
        nonlocal fibonacci_list
        if number <= len(fibonacci_list):
            return fibonacci_list[number - 1]
        else:
            for _ in range (len(fibonacci_list), number):
                next_number = fibonacci_list[-1] + fibonacci_list[-2]
                first_number = fibonacci_list[-1]
                second_number = next_number
                fibonacci_list.append(next_number)
            return fibonacci_list[-1]
    return get_next

fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                  55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

import time
time_start = time.perf_counter()
for number in range (15, 40):
    f1 = fibonacci(number)
    f1()
time_stop = time.perf_counter()
fibo_standard_time = time_stop - time_start
print (f'Standard Fibonacci timing: {fibo_standard_time:.7f} sec')

time_start = time.perf_counter()
for number in range (15, 40):
    f2 = fibonacci_memo(fibonacci_list, number)
    f2()
time_stop = time.perf_counter()
fibo_memo_time = time_stop - time_start
print (f'Memo Fibonacci timing: {fibo_memo_time:.7f} sec')
print (f'Memo times faster: {fibo_standard_time/fibo_memo_time:.2f}')

# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми
# елементів отриманого списку.
def f(number_list, users_function):
    final_list = []
    for element in number_list:
        if users_function(element):
            final_list.append(element)
    return sum(final_list)

sequince = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
result = f(sequince, lambda x: x > 0)
print(result)
