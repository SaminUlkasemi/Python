# Python also comes with a set of modules called the standard library. Each module is a Python 
# program that contains a related group of functions that can be embedded in your programs. For 
# example, the math module has mathematics- related functions, the random module has random 
# number–related functions, and so on
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners

import random, sys, os, math

for i in range(10):
    print(random.randint(20, 30))

# Alternative import style
# * With this form of import statement, calls to functions in random will not need the random. prefix
from random import *

while True:
    print("Type exit to exit")
    resp = input();
    if resp == "exit":
        sys.exit()
    print("You entered: ", resp)

