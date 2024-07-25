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

# ----------------------------- Keyword Arguments ---------------------------- #
# 131 page



