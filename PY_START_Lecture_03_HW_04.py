# Домашнє завдання № 4:
#
# 1. Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці.
# На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер квартири
# та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі.
# # Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.
num_flat = int(input('Please, enter flat number: '))
check_num_flat = (num_flat > 1 and num_flat < 144) or\
                 print ('There is no such flat number in this house')

num_entrance = not check_num_flat or print ('The number of entrance is: ', num_flat//36 + 1)

num_floor_1_3th = not check_num_flat or num_flat%36//4 == 0 or\
                  print ('The number of floor is: ', num_flat%36//4 + 1)
num_floor_4th = not check_num_flat or num_flat%36//4 != 0 or\
                  print ('The number of floor is: ', num_flat%36//4)

num_floor_flat_1_3 = not check_num_flat or not num_flat%4 or\
                print ('The number of flat on the floor is: ', num_flat%4, '\n')
num_floor_flat_4 = not check_num_flat or num_flat%4 or\
                print ('The number of flat on the floor is: ', 4, '\n')


# 2. Написати програму, яка буде повертати для заданого року кількість днів. Рік є високосним,
# якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.
num_year = int(input('Please, enter number of the year: '))
leap_year_days = not num_year%4 and num_year%100 and not num_year%400 and\
    print('Quantity days in the year: 366', '\n')
non_leap_year = not num_year%4 and num_year%100 and not num_year%400 or\
    print('Quantity days in the year: 365', '\n')

# 3. Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої.
# Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник.
a = int(input('Please, enter triangle side a: '))
b = int(input('Please, enter triangle side b: '))
c = int(input('Please, enter triangle side c: '))
check_for_exist = (a + b)> c and (a + c) > b and (b + c)> a and\
                  print('Triangle exists')
check_for_not_exist = ((a + b)> c and (a + c) > b and (b + c)> a) or\
                  print('Triangle doesn`t exist')
