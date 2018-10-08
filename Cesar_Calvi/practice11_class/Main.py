from Person import Person
from Employee import Employee

person = Person("cesar", "calvi", 23, 854752)
print person.name, "   ", person.last_name, "    ", person.age, "    ", person.ci

employe = Employee("cesar", "calvi", 23, 854752, "c4575-6", "System")
print employe.name, "   ", employe.last_name, "    ", employe.age, "    ", employe.ci, "  ", employe.employee_id, "   ", employe.department
