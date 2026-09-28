from Person import Person

class Employee:
    company_name = "Bitcode Tech"   #class level variable
    emp_cnt = 0

    # object level
    def __init__(self,name,salary,city):
        self.name = name
        self.salary = salary
        self.city = city
        Employee.emp_cnt = Employee.emp_cnt + 1

    def increment_salary(self,percentage):
        self.salary += self.salary * percentage
        print(self.salary)

    def display(self):
        print("display method of Employee class is called",self.salary)

    @classmethod
    def calculate_emp_cnt(cls):
        print("calculate_emp_cnt method of Employee class is called",cls.emp_cnt,"--",cls.company_name)


e = Employee("Abc", 100000.34, "Pune")
e2 = Employee("Xyz", 100330.34, "Pune")
print(type(e))
e.display()
e.increment_salary(0.4)

print("-----------------------------")
Employee.calculate_emp_cnt()
