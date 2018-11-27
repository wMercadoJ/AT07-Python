from Ana_Mamani.person import *


class Employee(Person):

    def __init__(self, name, last_name, age, ci, employee_id, departament):
        Person.__init__(self, name, last_name, age, ci)
        self.employee = employee_id
        self.departament = departament

    def get_employee(self):
        return self.personal_information() + " " + self.employee


instance_person = Person("elmer", "martinez", 25, 46460)
instance_employee = Employee("meyco", "martinez", 25, 46460, "4561", "Quimica")

print(instance_person.personal_information())
print(instance_employee.get_employee())
