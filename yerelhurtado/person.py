class Person:

    def __init__(self, first, last, age, ci):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.ci = ci

    def name(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        return self.age

    def get_ci(self):
        return self.ci