from Person import Person


class Employee(Person):
    """docstring for Employee"""
    def __init__(self, name, last_name, age, ci, employee_id, departament):
        Person.__init__(self, name, last_name, age, ci)
        self.employee_id = employee_id
        self.departament = departament

    def get_employee_id(self):
        return self.employee_id

    def get_department(self):
        return self.departament
