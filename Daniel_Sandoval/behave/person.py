# Implement the class Person and the subclass employee considering that person will have :
#   Name
#   Last Name
#   Age
#   CI


class Person:

    def __init__(self, first_name, last_name, age, ci):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ci = ci

    def Name(self):
        return self.first_name + " " + self.last_name + " " + self.age + " " + self.ci
