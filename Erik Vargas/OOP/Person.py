class Person:
    """docstring for Person"""
    def __init__(self, name, last_name, age, ci):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.ci = ci

    def get_complete_name(self):
        return self.name + " " + self.last_name
