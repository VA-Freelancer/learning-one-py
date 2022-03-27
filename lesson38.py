# Полиморфизм(мнодественные формы) - способность изменять, дополнять методы и свойства

from classes import Person, Employee

person2 = Person('Katy', 30)
# print(person2.age)
# person2.age = 32
# person2.print_info()

print(person2)

employee = Employee('Nick', 30, 'Yandex')
employee.print_info()
employee.more_info()

print(employee)