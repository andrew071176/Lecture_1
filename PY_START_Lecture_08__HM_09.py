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
def f5() -> str:
    # num = input('Please, enter sum in USD no more than 1 billion: ')
    # while num.isalpha() or float(num) > 10**10:
    #     num = input('Please, enter correct sum in USD no more than 1 billion: ')
    # num = f'{float(num):.2f}'

    dict_units = {'.': '', ' .0': 'zero', '0': '', '00': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                  '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
                  '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
                  '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen',
                  '20': 'twenty', '30': 'thirty', '40': 'fourty', '50': 'fifty',
                  '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'}

    num = 5100000.10
    num_str = '{0:,}'.format(float(num)).replace(',', ' ').replace('.', ' ') #digit division
    print (num_str)
    num_list = list(num_str.split(' '))                                         #list of digit divisions
    print (num_list)

    dict_division = {0: 'million(s)', 1: 'thousand(s)', 2: 'dollar(s)', 3: 'cent(s)'}
    for division in range (0, 4):
        if len(num_list[division]) == 3:
            print (dict_units[num_list[division][0]], end = ' ')
            if bool(num_list[division][0]):
                print (' hundred(s)')
            if int(num_list[division][1:]) in dict_units:
                print(dict_units[num_list[division][1:]], end = ' ')
            else:
                print(dict_units[str(int(num_list[division][1] * 10))] +\
                      ' ' +\
                      dict_units[num_list[division][2]], end = ' ')
        elif len(num_list[division]) == 2:
            if int(num_list[division]) in dict_units:
                print(dict_units[num_list[division]], end = ' ')
            else:
                print(dict_units[str(int(num_list[division][0]) * 10)] +\
                      ' ' +\
                      dict_units[num_list[division][1]], end = ' ')
        else:
            print (dict_units[num_list[division][0]], end = ' ')
        print (dict_division[division], end = ' ')


    # print (dict_units[int(num_list[1:])] if dict_units[int(num_list[1:] in dict_units else:
    # print (dict_units[int(num_list[1]*10)] + dict_units[int(num_list[2])





f5()


# 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22
# Докладніше: https://en.wikipedia.org/wiki/Roman_numerals

# 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22
# Докладніше: https://en.wikipedia.org/wiki/Roman_numerals
