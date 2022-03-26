# словари - хеш таблицы, ассоциативные спискм(массивы)
# from itertools import product

# d = {} # пустой словарь
# product1 = {'title': 'Sony', 'price': 100 } # большие объекты(словари) можно переносить на следующую строчку
# product2 = dict(title='iPhone', price=100) # создаем словарь через конструктор

# users = [
#     ['bob@gmail.com', 'Bob'],
#     ['katy@gmail.com', 'Katy'],
#     ['john@gmail.com', 'John']
# ] # переводим список в словарь, первое ключ второе значение
# d_users = dict(users)
# print(d_users)
# # print(product1)
# print(product1)
# print(product2)
# users_t = (
#     ('bob@gmail.com', 'Bob'),
#     ('katy@gmail.com', 'Katy'),
#     ('john@gmail.com', 'John')
# ) # создаем кортеж и получаем из него словарь
# t_users = dict(users_t)
# print(t_users)
# print(users_t)
# product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
# print(product3)

# nums = {i: i + 1 for i in range(1, 10)}
# product1 = {'title': 'Sony', 'price': 100 }
# product2 = dict(title='iPhone', price=100)
# print(product1['title'])
# print(product1.get('title2', 'NO')) # получили знанеи методом гет - если нет значения по ключу выведит none - может принимать дефолтное значение вторым параметром

# for key in product1:
#     print(key)
#     print(f'{key}: {product1[key]}')

# print(product1.items())
# for key, value in product1.items():
#     print(key, value)
# products = [
#     {'title': 'Sony', 'price': 90 },
#     {'title': 'IPhone', 'price': 110 },
#     {'title': 'Samsung', 'price': 70 }
# ]
# print(products)
# for product in products:
#     print(product['title'], product['price'])