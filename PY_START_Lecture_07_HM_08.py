# 1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".
dict_week_days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday',
                 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
num_day = int(input('Please, number of the week`s day: '))
print ('The name of the week`s day is: ', dict_week_days[num_day], '\n')

# 2. Опишіть кота (домашня тварина) на основі словника.
dict_cat = {'sex': 'male',
           'age': '3 years old',
           'coloring': 'red',
           'weight': '5 kg',
           'character': 'lazy'}

# 3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику,
# скільки разів яка літера зустрічається в цьому рядку.
# Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.
text = input('Please, enter text: ')
dict_letters = {}
for item in text:
    if item.isalpha() and item not in dict_letters:
        dict_letters[item] = text.count(item)
print ('The letters frequency in the text is:\n', dict_letters, '\n')

# 4. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери,
# які є одночасно і в першому, і в другому рядку.
# Наприклад, для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».
set_string_1 = set(input('Please, enter string 1: '))
set_string_2 = set(input('Please, enter string 2: '))
print ('The same_letters are: ',
       [letter for letter in set_string_1&set_string_2 if letter.isalpha()], '\n')

# 5. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.
list_multiple_of_3 = list(num*3 for num in range (20))
list_multiple_of_5 = list(num*5 for num in range (10))

# 6. Створіть список із числами, які є в обох списках.
list_multiple_of_3 = list(num*3 for num in range (20))
list_multiple_of_5 = list(num*5 for num in range (10))
list_multiple_of_3_and_5 = list(set(list_multiple_of_3)&set(list_multiple_of_5))