# 1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї
# літери R, за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
import re
string = 'Rbbbbbrrrr RRRbr RBr'
pattern = r'Rb*r'
match = re.findall(pattern, string)
if match:
    print(match)
else:
    print("pattern not found")

# 2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
import re
def validation_bank_card_number(string):
    pattern = r'(\d{4}-){3}\d{4}'
    match = re.match(pattern, string)
    if match:
        return True
    else:
        return False

string1 = '9999-9999-9999-9999'
string2 = '09999-9999-9999-9999'
string3 = '9999-9999-9999--9999'
print (validation_bank_card_number(string1))
print (validation_bank_card_number(string2))
print (validation_bank_card_number(string3))

# 3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.
import re
def validation_email(string):
    pattern = r'(^[a-zA-Z0-9]+' \
              r'([-]{,1})' \
              r'[a-zA-Z0-9_]+' \
              r'([-]{,1})' \
              r'@[a-zA-Z0-9-_]+' \
              r'.[a-zA-Z0-9-]+$)'
    match = re.match(pattern, string)
    if match:
        return True
    else:
        return False

string1 = 'aBCd_123-@gmail.com'
string2 = 'aBCd-_123@gmail.com'
string3 = 'aBCd123--@gmail.com'
string4 = '-aBCd123-@gmail.com'
print (validation_email(string1))
print (validation_email(string2))
print (validation_email(string3))
print (validation_email(string4))

# 4. Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів,
# що містить лише літери та цифри.
import re
def validation_login(string):
    pattern = r'[\d\w]{2,10}'
    match1 = re.match(pattern, string)
    if match1 and len(match1.group()) == len (string):
        return True
    else:
        return False

string1 = 'a1bc123456'
string2 = '123-5678ab'
string3 = 'abcd*12345'
print (string1, '=', validation_login(string1))
print (string2, '=', validation_login(string2))
print (string3, '=', validation_login(string3))