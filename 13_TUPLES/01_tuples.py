# Tuples are immutable sequences in Python
# They are defined using parentheses ()
# Example:


a = (3, 2, 22, 13)
print(a)
print(a[2])

a[3] = 12  # This will raise an error because tuples are immutable


b = (3, )  # a comma is needed for single-element tuples