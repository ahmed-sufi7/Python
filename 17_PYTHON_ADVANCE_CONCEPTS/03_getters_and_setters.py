class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property # property decorator is used to define a getter method. here the First_name becomes a property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

    @first_name.setter  # here the setter method is defined for the first_name property
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


    
        

e = employee("John Doe", 50000)
# print(e.first_name())
# e.set_first_name("Jack")
# print(e.name)

print(e.first_name)
first_name = "Jack" 
print((e.name))