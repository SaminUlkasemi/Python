# ---------------------------------------------------------------------------- #
#                                   Namespace                                  #
# ---------------------------------------------------------------------------- #
# Ref: https://realpython.com/python-namespaces-scope/

# ---------------------------- built-int namespace --------------------------- #
print(dir(print())) 

# ----------------------------- global namespace ----------------------------- #
print("global namespace".center(70, '-'))
myVar = "Python"
print(globals())

# accssing global namespace
print("globals()['myVar']: ", globals()['myVar'])

#
def a():
    var = "a"
    def b():
        var = "b"    
        def c():
            var = "c"
            print(var)
        c()
    b()
a()    

# ------------------------------ Local namespace ----------------------------- #
print("Local namespace".center(70, '-'))
print(locals())

# local namespace inside function
def func(a, b):
    def foo():
        print("")
    print("func namespace: ", locals())
    
func(10, 20)


a : str  = "samin"