# позиционные и именновонные аргументы функции
# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d

# print(get_sum(1, 2,d=4, c=2))


# перменно количество аргументов
# *args - будет преобразован в кортеж  - позиционные элементы
# **kwargs - ключевые слова(проще говря словарь) - именновонные элементы
# def get_sum(*args, **kwargs):
# def get_sum(*args):
#    return sum(args)
    
# print(get_sum(1, 5, 9))


# def func(**kwargs):
#     print(kwargs)
    
# func(a=1, b=5, c=20)


def f(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)
    
f(1, 2, 3, 4, b='test', c='hi')
f(1, 2)