# lambda-функция

# def get_square(num):
#     return num ** 2

# print(get_square(4))


# get_square = lambda num: num ** 2


# print(get_square(4))


# print((lambda num: num ** 2)(10))

from re import L


l = [1, 2, 3]


def get_double(l):
    return list(map(lambda num: num * 2, l))


print(get_double(l))