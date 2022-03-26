print('Таблица умножения')

def get_table(the_num):
    for i in range(the_num, 10):
        for k in range(2, 10):
            print(f'{i} * {k} = {i * k}\t') 
        print('')
    else:
        print('Well done')
        
        
def get_number():       
    while True:
        user_num=int(input('Укажите число 1 до 10'))
        if user_num > 10:
            print(f'Вы указали {user_num}, оно больше требуемого числа')
        elif user_num == 0:
            print(f'Вы указали {user_num}, оно не корректно')
        else:
            get_table(user_num) 
            break

get_number()
