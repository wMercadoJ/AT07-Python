from Person import Person


class Employee(Person, object):

    def __init__(self, name, last_name, age, ci, employee_id, department):
        super(Employee, self).__init__(name, last_name, age, ci)
        self.employee_id = employee_id
        self.department = department
