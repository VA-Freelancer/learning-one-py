class Person:
    # _ - приватная перменная на уровне соглашения  доступна извне | __ не доступна извне простыми способами, только специальными
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def print_info(self):
        print(f'Name {self.name}, Age {self.__age}')

    # def get_age(self):  # геттер
    #     return self.__age
    
    # def set_age(self, value):  # сеттер
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('Wrong age')
    #декоратор
    @property 
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')

    def __str__(self):
        # return f'Name: {self.name}'
        return 'Class: ' + self.__class__.__name__


class Employee(Person):
    
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company
    
    def more_info(self):
        print(f'Name {self.name}, works in {self.company}')
        
    def print_info(self):
        super().print_info()
        print(f'Work: {self.company}')
    
