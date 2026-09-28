class Person:
    def __init__(self,name,city):
        print("init method of person class called", name, "--", city)
        self.name = name
        self.city = city

    def display(self):
        print("display method of person class called", self.name, "--", self.city)