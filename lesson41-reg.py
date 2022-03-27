# регулярные выражения
import re

# s = 'Это просто строка текста. А это еще одна строка текста.'
# pattern = 'строка'

# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No matched')

# match = re.search(pattern, s)

# print(match.start())
# print(match.end())


# print(re.match(pattern, s))

# print(re.findall(pattern, s))

# print(re.split(r'\.', s, 1)) , ٣

# s = '''Это просто строка текста.
# А это ещё одна строка текста.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10 , ٣
# А это строка с разными символами: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string'''


# pattern = r'\w+'
# pattern = r'[эт]'
# pattern = r'[а-яё]+'
# pattern = r'[0-9]+'
# pattern = r'\d+'
# pattern = r'[\d-]+'
# pattern = r'\w+$'
# pattern = r'^\w+$'

# print(re.findall(pattern, s, flags=re.IGNORECASE))

email = 'mail@gmail.com'
def validate_email(email):
    # return re.match(r'^.+@(\w+\.)[a-z]{2,6}$', email, re.IGNORECASE)
    return bool(re.match(r'^.+@(\w+\.)[a-z]{2,6}$', email, re.IGNORECASE))

print(validate_email('mail1@outlook.com'))
print(validate_email('vproger@bank'))
print(validate_email('mail22@gmail.ru.com'))
