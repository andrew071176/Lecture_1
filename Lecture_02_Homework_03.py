#Homework_3
# 1. Write a Python program to print the number entered by user only if the
# number entered is negative.
number = float(input('Please, input number: '))
check = bool(number >= 0) or print (f'You`ve entered a negative number {number}\n')
check = bool(number < 0) or print (f'You`ve entered a not negative number!!!\n')

# 2. Write a Python program to check if the value a is less than 20 or not.
a = float(input('Please, input variable a: '))
check = bool(a >= 20) or print ('Variable a is less than 20\n')
check = bool(a < 20) or print ('Variable a is not less than 20\n')

# 3. Write a Python program to check if a given number is Zero or Not.
number = float(input('Please, input number: '))
check = bool(number != 0) or print (f'You`ve entered a number Zero\n')
check = bool(number == 0) or print (f'You`ve entered not Zero\n')

# 4. Write a Python program to check if a given number is Even or Odd.
number = float(input('Please, input number: '))
check = bool(number%2 != 0) or print (f'You`ve entered an Even number\n')
check = bool(number%2 == 0) or print (f'You`ve entered an Odd number\n')

# 5. Write a Python program to find largest number among three numbers
# entered by user.
number_1 = float(input('Please, input number 1: '))
number_2 = float(input('Please, input number 2: '))
number_3 = float(input('Please, input number 3: '))

check_for_number_1 = number_1 >= number_2 and number_1 >= number_3 and\
                      print (f'Number 1 ({number_1}) is the largest number')
check_for_number_2 = number_2 >= number_1 and number_2 >= number_3 and\
                     print (f'Number 1 ({number_2}) is the largest number')
check_for_number_3 = number_3 >= number_1 and number_3 >= number_2 and\
                     print (f'Number 1 ({number_3}) is the largest number')