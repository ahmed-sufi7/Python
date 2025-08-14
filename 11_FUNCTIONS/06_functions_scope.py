def sum(a, b):
    # Local variable
    c =  a + b
    z =1 # it creates a local variable which is desteroyed after function is called
    return c



def greet():
    z=8 # Local variable
    print("Hello")

z = 5  # Global variable
print(sum(4, 5))
print(z)
