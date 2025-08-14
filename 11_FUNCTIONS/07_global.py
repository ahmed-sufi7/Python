def sum(a, b):
    print("I am summing")
    c = a + b
    global z  # Modify global z
    z = 0
    return c

z = 2
print(sum(3, 12))
print(z)