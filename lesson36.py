# конструкторы классов - инкапсуляция 

from classes import Person
# import classes


person1 = Person('John')
person1.print_info()


person2 = Person('Katy')
# person2.__age = 30
# person2.print_info()
# print(person2.get_age())
# person2.set_age( 33)
# person2.print_info()
print(person2.age)
person2.age = 32
person2.print_info()
# print(person2._Person__age) #  доступ к инкапусулированному свойству