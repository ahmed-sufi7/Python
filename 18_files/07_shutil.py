import shutil
# shutil.rmtree("dir") # This will remove the directory 'dir' and all its contents whether it is empty or not
# shutil.copy("Harry.txt", "Harry2.txt")
shutil.move("Harry2.txt", "dir/Harry2moved.txt")