# ---------------------------------------------------------------------------- #
#                                   Decorator                                  #
# ---------------------------------------------------------------------------- #
# Link: https://www.programiz.com/python-programming/decorator


# ---------------------------------------------------------------------------- #
#                            @ Symbol With Decorator                           #
# ---------------------------------------------------------------------------- #
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
    
ordinary()

# ---------------------------------------------------------------------------- #
#                               passing argument                               #
# ---------------------------------------------------------------------------- #
def skip_divider_by_zero(func):
    def inner_divide(a, b):
        if b == 0:
            print("Can't divide by 0")
            return 
        return func(a, b)
    return inner_divide

@skip_divider_by_zero
def divider(a, b):
    return a / b

print(divider(1, 2))
print(divider(1, 0))










# ---------------------------------------------------------------------------- #
#                                class decorator                               #
# ---------------------------------------------------------------------------- #