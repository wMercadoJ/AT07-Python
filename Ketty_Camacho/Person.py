class Person:

    def __init__(self, first, last, age, ci):
        self.first_name = first
        self.last_name = last
        self.age_user = age
        self.ci_user = ci

    def name(self):
        return self.first_name + "," + self.last_name + "," + self.age_user + " ," + self.ci_user
