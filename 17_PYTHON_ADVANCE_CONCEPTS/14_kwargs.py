def marks(**kwargs):
    for items in kwargs.items(): # Kwargs are dictionaries 
        print(f"The marks of {items[0]} is {items[1]}")

marks(shubam = 90, rahul = 85, priya = 95)
