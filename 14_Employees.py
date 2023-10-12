
class Employees:
    Company = 'ABC.pvt.lmt'
    # constructor
    def __init__(self, name, email, dept, salary):
        self.name = name
        self.email = email
        self.dept = dept
        self.salary = salary

    def emp_info(self):
        print(f'Name is: {self.name}')
        print(f'Email is {self.email}')
        print(f'Department is {self.dept}')
        print(f'Salary is {self.salary}')

    def change_dept(self, new_dept):
        self.dept = new_dept
        print(f'Department changed to {new_dept}')


emp1 = Employees('Raju', 'raju@email.com', 'Sales', 50000)
emp2 = Employees('Sham', 'sham@email.com', 'QA', 75000)

emp1.emp_info()
emp2.emp_info()

emp1.change_dept('DevOps')
emp1.emp_info()
print(emp1.Company)

