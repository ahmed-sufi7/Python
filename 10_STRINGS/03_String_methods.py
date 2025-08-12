# name= "harry world" #strings in python are immutable

# # name[0] = "R" #You cannot do this

# a = len(name) #length of string
# print(a)

# print(name.upper(), name) 
# print(name.lower())
# print(name.capitalize()) #capitalize first letter
# print(name.title()) #capitalize first letter of each word

# 

# text = "Python is fun and fun and fun"
# print(text.find("is"))
# print(text.replace("fun","awesome"))

# text = "Apples,Bananas,pineapples"
# print(text.split(",")) #splits the string into a list at each comma
# print(",".join(["Apples", "Bananas", "Pineapples"])) #joins the list into a string with commas


text="Python123"
print(text.isalnum()) #checks if all characters are alphanumeric
print(text.isalpha()) #checks if all characters are alphabetic
print(text.isdigit()) #checks if all characters are digits
print(text.isspace()) #checks if all characters are whitespace