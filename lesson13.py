# цикл while

# i = 1
# while i <= 11:
#     print(i, end=' ')
#     i += 1

# print('hello', 'world', sep='_', end=' ')
# print('hello2', 'world2')
# s = 'Hello world'
# for l in s:
#     if l == ' ':
#         continue
#     print(f'"{l}"', end=' ')
# for i in 'Hello world':
#     if i == ' ':
#         break
#     print(i, end=' ')
# else:
#     print('\nNo spaces')
import datetime
now = datetime.datetime.now().year
year = 1900
while year <= now:
    print(f'{year} год')
    year += 1
else:
    print('Done;')