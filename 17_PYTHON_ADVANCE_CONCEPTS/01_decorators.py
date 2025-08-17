def decorator(func):
    def wrapper():
        print("Im Going to print a message")
        func()
        print("I have executed a function")
    return wrapper


@decorator
def say_hello():
    print("Hello!")

say_hello()

# f = decorator(say_hello)
# f() 