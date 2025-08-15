class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
            self.name = name

    def speak(self):
        print("speaking now...")

class Dog(Animal): # this is the inheritance 
    def speak(self):
        super().speak() # calling the parent class method
        print("Woof!")

# a = Animal("Dog")
# a.speak()

d = Dog("Buddy")
d.speak()
print(d.location)