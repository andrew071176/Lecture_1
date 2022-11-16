# 1. Реалізуйте функцію, параметрами якої є два числа та рядок.
# Повертає вона конкатенацію рядка із сумою чисел.
# def f1 (a: int, b: int, row: str) -> str:
#     return f'{a + b}' +  row

# 2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.
# def f2 (lenth: int, width: int) -> str:
#     print ('*' * width + '\n',
#            * ['*' + ' '*(width - 2) + '*\n' for _ in range (lenth)],
#            '*' * width + '\n', sep = '')

# 3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».
# def f3 (list_of_integers: list, x: int) -> int:
#     for i in range (len(list_of_integers)):
#         if list_of_integers[i] == x:
#             return i
#     return -1

# 4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.
# def f4 (text: str) -> int:
#     import string
#     for i in string.punctuation:
#         if i in text:
#             text = text.replace(i, '')
#     return len (text.split())

# 5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат.
# Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents
# def f5() -> str:
#     num = input('Please, enter sum in USD no more than 1 billion: ')
#     while num.isalpha() or float(num) > 10**10:
#         num = input('Please, enter correct sum in USD no more than 1 billion: ')
#     print()
#
#     dict_units = {'0': '', '00': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
#                   '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
#                   '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
#                   '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen',
#                   '20': 'twenty', '30': 'thirty', '40': 'fourty', '50': 'fifty',
#                   '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'}
#
#     #Forming number divisions list
#     num = f'{float(num):.2f}'
#     num_str = '{0:,}'.format(float(num)).replace(',', ' ').replace('.0', '.00').replace('.', ' ') #digit division
#     num_list = list(num_str.split(' '))                                         #list of digit divisions
#
#     #Putting numbers in words into string
#     dict_division = {3: 'million(s) ', 2: 'thousand(s) ', 1: 'dollar(s) ', 0: 'cent(s) '}
#     number_str = ''
#     for division in range (0, len(num_list)):
#         if len(num_list[division]) == 3:
#             number_str += (dict_units[num_list[division][0]] +\
#                            ' hundred(s) '*bool(int(num_list[division][0])))
#             if int(num_list[division][1:]) in dict_units:
#                 number_str += (dict_units[num_list[division][1:]] + ' ')
#             else:
#                 number_str += (dict_units[str(int(num_list[division][1]) * 10)] +\
#                       ' ' +\
#                       dict_units[num_list[division][2]] + ' ')
#         elif len(num_list[division]) == 2:
#             if int(num_list[division]) in dict_units:
#                 number_str += (dict_units[num_list[division]] + ' ')
#             else:
#                 number_str += (dict_units[str(int(num_list[division][0]) * 10)] +\
#                       ' ' +\
#                       dict_units[num_list[division][1]] + ' ')
#         else:
#             number_str += (dict_units[num_list[division][0]] + ' ')
#
#         #Adding number divisions names
#         if len(num_list) - 1 - division >= 2:
#             number_str += dict_division[num_list.index(num_list[len(num_list) - 1 - division])]*\
#                       bool(int(num_list[division]))
#         if len(num_list) - 1 - division == 1:
#             number_str += dict_division[num_list.index(num_list[len(num_list) - 1 - division])]
#         if len(num_list) - 1 - division == 0:
#             if num_list[division] != '00':
#                 number_str += dict_division[num_list.index(num_list[len(num_list) - 1 - division])]
#             else:
#                 number_str += '00 cents'
#
#     #print result
#     print (f'The number {num} in words are:\n', ' '.join(number_str.split()), sep = '')

# 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22
# Докладніше: https://en.wikipedia.org/wiki/Roman_numerals
def f6() -> int:
    dict_num_rome = {'I': ' 1 ', 'IV': ' 4 ', 'V': ' 5 ', 'IX': ' 9 ', 'X': ' 10 ',
                     'XL': ' 40 ', 'L': ' 50 ', 'XC': ' 90 ', 'C': ' 100 ',
                     'CD': ' 400 ', 'D': ' 500 ', 'CM': ' 900 ', 'M': ' 1000 '}

    num_rome = input('Please, enter rome number: ')
    # while (item for item in num_rome not in 'IVX'):
    #     num_rome = input('Please, enter correct rome number: ')

    num_arabic = num_rome
    for lenth in (2, 1):
        for key in dict_num_rome:
            if len(key) == lenth and key in num_arabic:
                num_arabic = num_arabic.replace(key, dict_num_rome[key]) #arabic numbers

    print (f'The rome number {num_rome} converted into arabic num is:',
           sum (int(i) for i in num_arabic.split()))
    # print ('num_arabic = ', num_arabic)

f6()
