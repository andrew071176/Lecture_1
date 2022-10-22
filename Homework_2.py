# 1. Construct an integer from the string "123"
print ('String "123" is converted into: ', int(123), type(int('123')), '\n')

# 2. Construct a float from the integer 123
print ('Integer 123 is converted into: ', float (123), type(float(123)), '\n')

# 3. Construct an integer from the float 12.345
print ('float 12.345 is converted into: ', int(12.345), type(int(12.345)), '\n')

# 4. Write a Python-script that detects the last 4 digits of a credit card
card_number = int (input('Please, input card number: '))
card_number_str = str(card_number)
print('The last 4 numbers of the card are: ', card_number_str[-4:], '\n')

# 5. Write a Python-script that calculates the sum of the digits of a three-digit number
number = int(input('Please, input three-digit number: '))
number_str = str(number)
sum = 0
for i in number_str:
    sum += int(i)
print ('The sum of the digits of a three-digit number is: ', sum, '\n')

# 6. Write a program that calculates and displays the area of a triangle if its sides are known
trg_side_1 = float(input('Please, input the lenth of the first triangle side: '))
trg_side_2 = float(input('Please, input the lenth of the second triangle side: '))
trg_side_3 = float(input('Please, input the lenth of the third triangle side: '))
semi_perimeter = (trg_side_1 + trg_side_2 + trg_side_3)/2
trg_area = (semi_perimeter*\
             (semi_perimeter - trg_side_1)*\
             (semi_perimeter - trg_side_2)*\
             (semi_perimeter - trg_side_3))**(1/2)
print ('The triangle area is: ', trg_area, '\n')

# 7. *Write a Python-script that calculates the sum of the digits of a number
number = int(input('Please, input number: '))
number_str = str(number)
sum = 0
for i in number_str:
    sum += int(i)
print ('The sum of the number digits is: ', sum, '\n')

# 8. *Determine the number of digits in a number
number = int(input('Please, input number: '))
number_str = str(number)
counter = 0
for i in number_str:
    counter += 1
print ('The number of digits in number is: ', counter, '\n')

# 9. *Print the digits in reverse order
number = int(input('Please, input number: '))
number_str = str(number)
print ('The number of digits in number is: ', number_str[::-1])