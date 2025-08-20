with open("Harry.txt", "r") as f:
    content = f.read()
    print(content) # This will print the entire content of Harry.txt and there is no need of f.close()