from functools import reduce

numbers = [1, 2, 3, 4, 5]

new = reduce(lambda x, y: x + y, numbers)
print(new)