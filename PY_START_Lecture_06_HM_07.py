# 1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.
text = input('Please, enter the text: ')
letter_x = input('Please, enter letter to be found in the text: ')
print (sum (int(letter_x == letter) for letter in text), '\n')

# 2. Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного ім'я
# на валідність (мається на увазі, що, наприклад, в імені людини не може бути цифр,
# воно повинно починатися з великої літери, за якою повинні йти маленькі).
name = input('Please, enter the person`s name: ')
while not (name.isalpha() and name.istitle()):
    name = input('Please, enter correct person`s name: ')
print()

# 3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.
text = input('Please, enter the text: ')
print ('The symbol codes sum of the string is: ', sum (ord(symbol) for symbol in text), '\n')

# 4. Виведіть на екран 10 рядків із значенням числа Pi. У першому рядку має бути 2 знаки після коми,
# у другому 3 і так далі.
import math
print (*(round(math.pi, i) for i in range(2, 12)), sep = '\n')
print()

# 5. Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.
import string
text = input('Please, enter the text: ')
for item in string.punctuation:
    while item in text:
        text = text.replace(item, '')
print ("The longest user's word is: ", max (text.split(), key = len), '\n')

# Додаткові задачі до домашнього завдання:
#
# 1. Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери).
# Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту.
# Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"
text = 'aaaaaaa  ititititit   catcatcatcat'
list_text =  text.split()
for i in range(len(list_text)):
    list_text[i] = list_text[i][:list_text[i].index(list_text[i][0], 1)]
print ('The shortest Vovochka`s word is: ', min(list_text, key = len), '\n')

# 2. Напишіть програму для очищення тексту від HTML-тегів.
# Більше про html-теги https://html5book.ru/html-tags/
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто,
# перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації.
# Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">
text = '''<div id="rcnt" style="clear:both;position:relative;zoom:1">'''
import re
pre_teglist = re.findall(r'</.*>', text)
final_teglist = pre_teglist + list(map(lambda i: i.replace('/', ''), pre_teglist)) + ['<', '>']
for teg in final_teglist:
    text = text.replace(teg,'')
print ('The text without tegs is:\n', text)