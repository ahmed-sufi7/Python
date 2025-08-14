marks = {"harry" : 85, "jack": 45, "lily": 78, "john": 90}

print(marks.keys()) 
print(marks.values())
print(marks.items())  # Accessing key-value pairs
print(marks.pop("lily"))

marks.clear()

print(marks)