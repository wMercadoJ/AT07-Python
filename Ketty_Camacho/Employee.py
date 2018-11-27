from Ketty_Camacho.Person import *


class Employee(Person):
    def __init__(self, first, last, age, ci, id, departament):
        Person.__init__(self, first, last, age, ci)
        self.employee_id = id
        self.employee_departament = departament

    def GetEmployee(self):
        return self.Name() + "," + self.employee_id + "," + self.employee_departament


objet_person = Person("tatina", "garcia", "20", "6485712")
objet_employee = Employee("ramiro", "paco", "20", "456285", "5555", "physic")

print(objet_person.name())
print(objet_employee.GetEmployee())
