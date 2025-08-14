marks = [85, 90, 78, 92, 88]
extra_marks = [95, 89]

print(marks)
marks.append(95)  # This will change the original list
print(marks)

marks.pop()
print(marks)
marks.extend(extra_marks)
print(marks)