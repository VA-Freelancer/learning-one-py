#OOP  объектно орентирования программирования object orientier programm
# переменная созданная в классе - свойство
# функция описанная внутри класса = метод
class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'guest'
    
    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name



a = A()
b = A()


# a.property1 = 'Property 1'
# a.property2 = 'Property 2'

# print(a)
print(a.property2)
print(a.say_hi(''))