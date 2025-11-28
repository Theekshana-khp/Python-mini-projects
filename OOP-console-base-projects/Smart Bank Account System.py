def  add(a,b):
    return a+b

print(add(1,2))

#class

class Person:
    def __init__(self , name ,age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f'your name is {self.name}')

person = Person('pasindu',20)
person.print_name()
