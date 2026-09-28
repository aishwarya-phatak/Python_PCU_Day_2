from Person import Person

class Student(Person):
    def __init__(self, name,city,roll_id):
        print("init method of Student class is called")
        super().__init__(name,city)
        self.roll_id = roll_id

    def display(self):
        print("display of student", self.roll_id)

s = Student("Xyz","Pune",12311)
s.display()