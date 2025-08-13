'''
Two types of modules in Python:
1. Built-in modules (e.g., math, sys)
2. User-defined modules

'''

import math  # built-in 
import os
import mymodule   # user-defined module
import requests  # external library

print(math.sqrt(16))  # Example of using a module
mymodule.hello()
r = requests.get("https://google.com")
print(r.text)
