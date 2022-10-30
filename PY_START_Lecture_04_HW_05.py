# Домашнє завдання (має бути виконано з zip, all, map; for - зайвий):
# 1. Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
# Примітка: щасливим квитком називається число, у якому, при парній кількості цифр,
# сума цифр його лівої половини дорівнює сумі цифр його правої половини.
# Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.
num = str(input('Please, enter number with paired quantity of digits: '))
while len(num)%2:
    print ('Wrong entered number')
    num = str(input('Please, enter number with paired quantity of digits: '))
left_list = list(map(int, num[:len(num)//2]))
right_list = list(map(int, num[len(num)//2:]))
if sum(left_list) == sum (right_list):
    print('The number is lucky', '\n')
else:
    print('The number is not lucky', '\n')

# 2. З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
# Примітка: Паліндром називається число, слово або текст, які однаково читаються зліва направо
# і справа наліво.
# Наприклад, це числа 143341, 5555, 7117 і т.д.
num = str(input('Please, enter number/word: '))
num_initial_list = list(map(int, num))
num_reverse_list = num_initial_list[::-1]
if num_initial_list == num_reverse_list:
    print ('You`ve entered palindrome number/word', '\n')
else:
    print('You`ve entered not palindrome number/word', '\n')


# 3. Дано коло з центром на початку координат та радіусом 4.
# Користувач вводить з клавіатури координати точки x та y.
# Написати програму, яка визначить, лежить ця точка всередині кола чи ні.
x, y = float(input('Please, enter coordinate x: ')),\
       float(input('Please, enter coordinate y: '))
R = 4
if pow(x, 2) + pow (y, 2) <= pow(R, 2):
    print ('The point inside the circle')
else:
    print('The point outside the circle')