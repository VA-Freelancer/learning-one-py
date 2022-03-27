"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно.
Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""


def find_sum(n):
    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res+= i
    return res


print(find_sum(5) ) # return 8 (3 + 5)
print(find_sum(10))  # return 33 (3 + 5 + 6 + 9 + 10)

def find_sum2(n):
    return sum(i for i in range( n + 1) if i % 3 == 0 or i % 5 == 0)

print(find_sum2(5) ) # return 8 (3 + 5)
print(find_sum2(10))  # return 33 (3 + 5 + 6 + 9 + 10)
