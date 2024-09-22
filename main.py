class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name:", self.name, "ID:", self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post
        employee1 = Employee("Rayan", "1770", 100000, "Spacescientist" )
        employee1.display()