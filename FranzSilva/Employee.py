from FranzSilva.Person import Person


class Employee(Person):
    def __init__( self, name, last_name, age, ci, employee_id, department ):
        super().__init__(name, last_name, age, ci)
        self.employee_id = employee_id
        self.department = department


employee = Employee('franz', 'Milan', 2, 796521, 111111,'develop')
print(employee.name, employee.last_name, employee.department)
