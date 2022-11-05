# 1. Написати Python-скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7.
print('The numbers divisible by 7 from 1 to 100:')
for num in range (1, 101):
    if not num%7:
        print(num, end = ' ')
print('\n')

# 2. Написати Python-скрипт, який обчислює за допомогою циклу факторіал числа n
# (n вводиться з клавіатури).
num = int(input('Please, enter integer number: '))
print (f'Factorial of number {num} ', end ='')
product = 1
while num > 1:
    product *= num
    num -= 1
print (f'is {product}', '\n')
#
# 3. Написати Python-скрипт, який виводить на екран таблицю множення на 5.
# Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...
num = int(input('Please, enter integer number: '))
print (f'Multiplication tab for number {num}:')
for i in range (1, num + 1):
    print(f'{i} x {num} = {i*num}')
print()
#
# 4. Написати Python-скрипт, який виводить на екран прямокутник із '*'.
# Висота і ширина прямокутника вводяться з клавіатури.
# Наприклад, нижче представлений прямокутник з висотою 4 та шириною 5.
# *****
# *      *
# *      *
# *****
width, height = int(input('Please, enter width of the rectangle: ')),\
                int(input('Please, enter height of the rectangle: '))
for i in range(1, height + 1):
    if i == 1 or i == height:
        print(width*'*')
    else:
        print('*' + (width - 2)*' ' + '*')
print()

# 5. Є список [0,5,2,4,7,1,3,19]. Написати Python-скрипт для підрахунку непарних цифр у ньому.
list_1 = [0,5,2,4,7,1,3,19]
counter = 0
for num in list_1:
    if num%2:
        counter += 1
print (f'The quantity of odd numbers in list is {counter}', '\n')

#
# 6. Створіть список випадкових чисел (розміром 4 елементи).
# Створіть другий список у два рази більше першого, де перші 4 елементи повинні дорівнювати
# елементам першого списку, а решта елементів - подвоєним значенням початкових.
# Наприклад,
# Було → [1,4,7,2]
# Стало → [1,4,7,2,2,8,14,4]
import random
list_1 = [random.randint(1, 10) for _ in range(4)]
list_2 = [item*2 for item in list_1]
print('The final list is:', list_1 + list_2, '\n')

#
# 7. Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць.
# Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.
list_salary = [random.randint(10_000, 14_000) for _ in range(12)]
print ('The salary list is: ', list_salary)
print('The average salary is: ', format(sum(list_salary)/len(list_salary), '.2f'), '\n')


# 8. Є матриця
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9,10, 11, 12]
# [13,14, 15, 16]
# Напишіть Python-скрипт, який виведе цю матрицю на екран, обчислить
# та виведе суму елементів цієї матриці.
list_matrix = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9,10, 11, 12],
               [13,14, 15, 16]]
print ('Input matrix: ', list_matrix)
sum_list_matrix = 0
for item in list_matrix:
    sum_list_matrix += sum(item)
print ('The matrix elements sum is: ', sum_list_matrix, '\n')

#
# 9. Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
# Список може бути довільною довжиною.
list_1 = [7, 2, 9, 4]
print ('The input list: ', list_1)
for i in range (len(list_1)//2):
    list_1[i], list_1[len(list_1) - 1 - i] = list_1[len(list_1) - 1 - i], list_1[i]
print ('The mirror list is: ', list_1, '\n')

#
# 10. За допомогою циклів вивести на екран усі прості числа від 1 до 100.
prime_numbers_list = []
for i in range (2, 101):
    for j in range (2, i):
        if i%j == 0:
            break
    else:
        prime_numbers_list.append(i)
print ('The prime numbers from 1 to 100 is:\n', *prime_numbers_list, '\n')

#
# 11. Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури
# (число непарне). У прикладі ширина дорівнює 5.
# *****
#  ***
#   *
#  ***
# *****
clock_width = int(input('Please, input the clock width (odd number): '))
indent = 0
for i in range (clock_width, 0, -2):
    print (indent * ' ', (i * '*'))
    indent += 1
indent = clock_width//2 - 1
for j in range (3, clock_width + 1, 2):
    print(indent * ' ', j * '*')
    indent -= 1


