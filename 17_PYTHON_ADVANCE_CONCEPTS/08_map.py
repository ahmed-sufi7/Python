number = [1, 2, 3, 4, 5]

def square(x):
    return x * x 

new = map(square, number)
print(list(new))