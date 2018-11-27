class Person:

    def __init__(self, name, last_name, ci, age):
        self.name = name
        self.last_name = last_name
        self.ci = ci
        self.age = age


person = Person('Franz', 'Silva', 00, 785478)
print(person.ci, person.last_name, person.name)