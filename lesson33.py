# ошибки и их исключения
# print('Hello')

# try:
#     num = 100/2
# except Exception:
#     num = 0
# else:
#     print('Успешно')
# finally:
#     print('В любом случае')
    
# print(num)

while True:
    try:
        num = int(input('Enter your number: '))
        print(f'100/ {num} = {100 / num}')
        break
    except ZeroDivisionError:
        print('The number must be greater than zero.')
    except ValueError:
        print('Must be a number')