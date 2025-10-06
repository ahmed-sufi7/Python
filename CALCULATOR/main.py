try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("what kind of operation you want to perform: ")
    print (" Press + for addition\n press - for subtraction\n Press * for multiplication\n Press / for division")

    o = input("enter the operation: ")

    match o:
        case '+':
            print(f"The result is: {a + b}")
        case '-':
            print(f"The result is: {a - b}")
        case '*':
            print(f"The result is: {a * b}")
        case '/':
            print(f"The result is: {a / b}")
        case _:
            print("Invalid operation")

except Exception as e:
    print ("Enter the valid operation", e)