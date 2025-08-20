#dunder methods are special methods in Python that have double underscores at the beginning and end of their names.
class employee:
    company = "Tech Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"
    
    def __repr__(self):  # mostly used by developers to debug
        return f"employee(name={self.name}, salary={self.salary})"
    
    def __len__(self):
        return len(self.name)

e = employee("John Doe", 50000)
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))  # This will call the __repr__ method 

print(len(e))