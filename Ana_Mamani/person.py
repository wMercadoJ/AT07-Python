class Person:

    def __init__(self, name, last_name, age, ci):
        self.names = name
        self.last_names = last_name
        self.ages = age
        self.c_i = ci

    def personal_information(self):
        return self.names + " " + self.last_names + " " + str(self.ages) + " " + str(self.c_i)
