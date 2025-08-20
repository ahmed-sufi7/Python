import os

a = os.listdir("dir")
print(a)

print(os.getcwd()) # This will print the current working directory
print(os.path.exists("dir"))
os.remove("sample1.txt")
os.rmdir("dir") # This will remove the directory 'dir' if it is empty
