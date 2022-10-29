#HOMEWORK 1
# Excercise 1. Write a Python-script that displays the message “Hello world”.
print ('Hello, World\n')

# Excercise 2. Rewrite the first script to display three any messages.
print ('Hello, Father')
print ('Hello, Mather')
print ('Hello, Everyone\n')

# Excercise 3. Write a Python-script to reads values for the length and width of a
# rectangle and returns the area of the rectangle.
rect_width = float(input('Please, enter rectangle width: '))
rect_lenth = float(input('Please, enter rectangle lenth: '))
print (f'The area of rectangle is: {rect_width*rect_lenth}\n')

# Excercise 4. Write a program that requests the user to enter two numbers and
# prints the sum, product, difference and quotient of the two numbers.
number_1 = float(input('Please, enter number 1: '))
number_2 = float(input('Please, enter number 2: '))
print (f'The sum of two numbers is: {number_1 + number_2}')
print (f'The product of two numbers is: {number_1 * number_2}')
print (f'The difference of two numbers is: {number_1 - number_2}')
print (f'The quotient of two numbers is: {number_1/number_2}\n')

# Exercise 5. Write a program that reads in the radius of a circle and prints the
# circle’s diameter, circumference and area. Use the constant value 3.14159 for π.
# Do these calculations in output statements.
circle_radius = float(input ('Please, enter radius of circle: '))
print (f'The circles`s diameter is: {circle_radius*2}')
print (f'The circumference is: {2*3.14159*circle_radius}')
print (f'The circle`s area is: {3.14159*circle_radius**2}')
