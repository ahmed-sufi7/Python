class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def sum(self, p):
        return point(self.x + p.x, self.y + p.y)

    def print_point(self):
        print(f"Point({self.x}, {self.y})")

    def __add__(self, p):
        return point(self.x + p.x, self.y + p.y)

p1 = point(2, 3)
p2 = point(4, 5)


# p3 = p1.sum(p2)
p3 = p1 + p2  # by using the __add__ method we overloaded the + operator
p3.print_point()