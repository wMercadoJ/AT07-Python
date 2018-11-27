# Employee will have :
#   Employee_Id
#   Department
# Define both classes into different modules
from Daniel_Sandoval.behave.person import Person


class Employee(Person):

    def __init__(self, first_name, last_name, age, ci, employee_id, departament):
        Person.__init__(self, first_name, last_name, age, ci)
        self.employee_id = employee_id
        self.departament = departament

    def get_eployee(self):
        return self.Name() + ", " + self.employee_id + ", " + self.departament


person = Person("Fulinito", "Conejitos", "444", "78787")
employee = Employee("Menganito", "Rabitos", "1007", "874521", "1111", "quimica")

print(person.Name())
print(employee.get_eployee())