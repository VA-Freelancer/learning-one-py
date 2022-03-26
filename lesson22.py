# # user function - что бы избекать дублирования кода? некий повторяющий блок кода

# def hello(name, word):
#     print(f"Hello, {name} say {word}")

# hello('John', 'Hi')
# hello('Ketty',  'Hello')
# hello('Andrey', 'GoodBy')


# def get_sum(a, b):
#     print(a + b)



# x = 20
# y = 30
# get_sum(2, 3)
# get_sum(x, y)


def get_sum(a, b):
    return a + b

print(get_sum(1, 2))