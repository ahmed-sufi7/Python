class employee:
    company = "Tech Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    #This is instance method
    def print_info(self):
        print(f"The Name is {self.name} and the salary is {self.salary}")

    #This is a static method
    @staticmethod #static method doesn't require self
    def sum(a,b): #Not passing self
        return a + b

    @classmethod #classmethod takes cls as the first argument
    def print_company(cls): #cls refers to the class 
        print(f"The company is {cls.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = employee("John Doe", 50000)
e2 = employee("Jane Smith", 60000)
# print(employee.company)
# print(employee.name) # this ewill throw error


e1.print_info()
e2.print_info()

print(employee.sum(10, 20))  # This will work because sum is a static method
print(e2.sum(10, 20))  # This will work because sum is a static method

employee.print_company()  # This will work because print_company is a class method
employee.change_company("ASUS")  # Change the company name
print(employee.company)  # This will work because company is a class variable