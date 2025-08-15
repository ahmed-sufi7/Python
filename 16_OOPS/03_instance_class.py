class employee: 
    company = "Asus"  # this is class attribute
    
    def __init__(self, name, salary, bond, company):  #constructor 
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company

    def get_salary(self):   # self is the way to refer a class which is being created 
        return self.salary
    
    def get_info(self):
        print(f"The name of the person is {self.name} and the salary is {self.salary} for the bond of { self.bond} years.")

e1 = employee("Ali", 600000, 3, "tesla") #tesla is the instance attribute
print(e1.company)
print(employee.company) # this will print the class attribute

# Object introspection
print(dir(e1)) 

