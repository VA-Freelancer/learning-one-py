words = ['мадам', 'топот', 'test', 'madam', 'world']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']

# polindromes = []
# for word in words:
#     # word[::-1] # переварачиваем строку
#     if word == word[::-1]:
#         polindromes.append(word)
# polindromes = [word for word in words if word == word[::-1]] # решение в одну строчку

polindromes = []
for str in my_str:
    str_r = str.replace(' ', '').lower() #убираем пробелы и приводим к нижнему регистру
    # word[::-1] # переварачиваем строку
    if str_r == str_r[::-1]:
        polindromes.append(str)