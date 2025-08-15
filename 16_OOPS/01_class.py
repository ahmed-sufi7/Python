# class is a blueprint or a template for creating objects eg, user registration form

# object is an instance of a class eg. form which contains the data for john 


class employee:
    company = "HP"

    def get_salary(self):   # self is the way to refer a class which is being created 
        return 340000

e = employee()  # An object is created
print(e.get_salary())   #  Employee e's salary
print(e.company)   #  Employee e's company


e2 = employee()
print(e2.get_salary())   #  Employee e2's salary
print(e2.company)   #  Employee e2's company
