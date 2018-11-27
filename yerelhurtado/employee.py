from yerelhurtado.person import *


class Employee(Person):
    def __init__(self, first, last, age, ci, staffnum, departament):
        super().__init__(first, last, age, ci)
        self.staffnumber = staffnum
        self.departament = departament

    def get_employee(self):
        return self.name() + ' , ' + self.staffnumber

    def get_departament(self):
        return self.departament


luis = Employee("Luis", "Alvares", "1000")
print(luis.get_employee())
