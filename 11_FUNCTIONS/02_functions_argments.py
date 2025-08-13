def add(a, b, plus=0):   #default argument 
    x = a + b + plus
    return x

c = add(3, 5, 5)
print(c)


c1 = add(b=5, a=3)  # keyword arguments
print(c1)