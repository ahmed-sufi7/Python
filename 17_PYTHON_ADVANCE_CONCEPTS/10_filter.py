def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = [1, 2, 3, 4, 5, 34, 24, 632, 45, 5, 2, 3, 57, 34]
new = filter(is_even,n)
print(list(new))