# Implement the class Person and the subclass employee considering that person will have :
# Name, Last Name, Age and CI

class Person:
    def __init__(self, name, last_name, age, ci):
        self.first_name = name
        self.last_name = last_name
        self.age = age
        self.ci = ci

    def get_name(self):
        return self.first_name + " " + self.last_name
