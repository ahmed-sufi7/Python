class employee:
    
    def __init__(self, name, salary, bond):  #constructor 
        self.name = name
        self.salary = salary
        self.bond = bond

    def get_salary(self):   # self is the way to refer a class which is being created 
        return self.salary
    
    def get_info(self):
        print(f"The name of the person is {self.name} and the salary is {self.salary} for the bond of { self.bond} years.")

e = employee("Ahmed", 500000, 2)
e.get_info()