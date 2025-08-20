# while True:
#     try: 
#         a = int(input("Enter a number 1: "))
#         b = int(input("Enter a number 2: "))

#         print(f"the division is {a/b}")
#     except ValueError as e:
#         print("Invalid input. Please enter numbers only.", e)
#     except Exception as e:
#         print("Some error occurred", e)
#     except ZeroDivisionError as e:
#         print("dont divide by zero!", e)


a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

if b==0:
    raise ValueError("Division by zero is not allowed.")

print(f"the division is {a/b}")