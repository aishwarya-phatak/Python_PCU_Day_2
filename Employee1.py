from Person import Person

class Employee1(Person):
    company_name = "Bitcode Tech"   #class level variable
    emp_cnt = 0

    # object level
    def __init__(self,name,city,salary):
        print("init method of Employee1 class is called")
        super().__init__(name,city)
        self.salary = salary
        Employee1.emp_cnt = Employee1.emp_cnt + 1

    def increment_salary(self,percentage):
        self.salary += self.salary * percentage
        print(self.salary)

    def display(self):
        print("display method of Employee1 class is called",self.salary)

    @classmethod
    def calculate_emp_cnt(cls):
        print("calculate_emp_cnt method of Employee class is called",cls.emp_cnt,"--",cls.company_name)


e = Employee1("Abc", "Pune",100000.34, )
e2 = Employee1("Xyz", "Pune",100330.34)
print(type(e))
e.display()
e.increment_salary(0.4)

print("-----------------------------")
Employee1.calculate_emp_cnt()
