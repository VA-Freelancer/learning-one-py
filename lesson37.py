# наследование
from classes import Person, Employee

person2 = Person('Katy', 30)
print(person2.age)
person2.age = 32
person2.print_info()

employee1 = Employee('Nick', 30)
employee1.print_info()
employee1.more_info()