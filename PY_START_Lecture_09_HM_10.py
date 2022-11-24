# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить
# рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.
#Function for checking arithmetic progression
def f1_1(list_1: list) -> int:
    difference = list_1[1] - list_1[0]
    for i in range (1, len(list_1)):
        if list_1[i] - list_1[i-1] == difference:
            if i == len(list_1) - 1:
                return list_1[i] + difference
        else:
            return False

#Function for checking geometric progression (multiplication)
def f1_2(list_1: list) -> int:
    if list_1[0] != 0:
        multiplier = int(f'{list_1[1]/list_1[0]:,.0f}')
        for i in range (1, len(list_1)):
            if list_1[i]/list_1[i-1] == multiplier:
                if i == len(list_1) - 1:
                    return list_1[i]*multiplier
            else:
                return False

#Function for checking geometric progression (exponentiation 2)
def f1_3(list_1: list) -> int:
    for i in range (len(list_1)):
        if (i + 1)**2 == list_1[i]:
            if i == len(list_1) - 1:
                return (i + 2)**2
        else:
            return False

#Function for checking geometric progression (exponentiation 3)
def f1_4(list_1: list) -> int:
    for i in range (len(list_1)):
        if (i + 1)**3 == list_1[i]:
            if i == len(list_1) - 1:
                return (i + 2)**3
        else:
            return False

def f1(f1_1, f1_2, f1_3, f1_4, list_1: list) -> int or bool:
    if f1_1(list_1):
        return f1_1(list_1)
    elif f1_2(list_1):
        return f1_2(list_1)
    elif f1_3(list_1):
        return f1_3(list_1)
    elif f1_4(list_1):
        return f1_4(list_1)
    else:
        return ('Error')

list_num = list(map(int, list(input('Please, enter sequence of numbers: ').replace(',', ' ').split())))
print (f1(f1_1, f1_2, f1_3, f1_4, list_num))

# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, множенням яких чисел він є.
def f2() -> str:
    for i in range (999_999, 100_000, -1):
        if str(i)[:3] == str(i)[-1:-4:-1]:
            for j in range (999, 100, -1):
                if not i%j and len(str(int(i/j))) == 3:
                    return f'Max 6-digit palindrome: {i}\nMultipliers: {j}, {int(i/j)}'
print (f2())
