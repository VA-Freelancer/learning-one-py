"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный). Определите, есть ли в списке число, которое
является индексом элемента "odd". Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""

def odd_ball(arr: object) -> object:
    return arr.index('odd') in arr




print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])) # False
print(odd_ball(["even",10,"odd",2,"even"])) # True

