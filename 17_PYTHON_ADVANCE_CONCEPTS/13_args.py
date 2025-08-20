def sum(*args):  # args will be the tuple of all arguments passed 
    total = 0
    for item in args:
        total += item
    return total

print(sum(5, 10, 34))