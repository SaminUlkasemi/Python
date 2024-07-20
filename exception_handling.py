# ---------------------------------------------------------------------------- #
#                              Exception Handling                              #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners

def division(divisor):
    try:
        return 10 / divisor
    except:
        print("Invalid argument")

print(division(10))
print(division(0))

# ----------------------------- Diffenet approch ----------------------------- #
# * Here division(5) will never executed, because once the execution jumps to the
# * code in the except clause, it does not return to the try clause. Instead, it 
# * just continues moving down as normal.
try:
    print(division(10))
    print(division(0))
    print(division(5))
except:
    print("Invalid argument")

