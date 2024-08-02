# ---------------------------------------------------------------------------- #
#                                   Function                                   #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners

def printMsg(name):
    print("Welcome to", name, "file")

printMsg("function")

# return from a function
def sum(a, b):
    return a + b

sum(10, 20)

# * Python adds return None to the end of any function definition with no return statement. 
def subs(x, y):
    x + y

print(subs(20, 10))

# * Using a return statement without a value (that is, just the return keyword by itself), then None is
# * returned.
def foo():
    return 

print(foo())

# function argument with default value
def func_def_val(x = 0, y = 0):
    return x + y

print("function with default value: ", func_def_val())

# function argument with type
def func(x:int, y:int):
    if type(x) != int:
        raise ValueError
    return x + y

print("function with argument: ",func(10, 10))

myFunc = func_def_val
print(myFunc())

# ----------------------------- Keyword Arguments ---------------------------- #
# 131 page



