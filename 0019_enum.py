# ---------------------------------------------------------------------------- #
#                                     Enum                                     #
# ---------------------------------------------------------------------------- #
# https://www.geeksforgeeks.org/enum-in-python/
# https://realpython.com/python-enum/

#* Because Enums are used to represent constants we recommend using 
#* UPPER_CASE names for enum members

from enum import Enum, auto

class Season(Enum):
    SPRING = 2
    SUMMER = 3
    AUTUMN = 4
    WINTER = 5

print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(list(Season))

# ------------------------------ Accessing Modes ----------------------------- #
# By value:- In this method, the value of enum member is passed.
# By name:- In this method, the name of the enum member is passed.
print(f'Value of Member 2 of enum: {Season(4).name}')
print(f'Value of Member 2 of enum: {Season(4).value}')
print(f'Value of Season["AUTUMN"]: {Season['WINTER'].value}')

# ------------------------------ Enum Iteration ------------------------------ #
for s in Season:
    print(s)
    
#! Because enumeration members must be constants, 
#! Python doesn’t allow you to assign new values to enum members at runtime:
try:
    Season.SPRING = 1
except Exception as e:
    print(e)
    
# ----------------------------- Enum using range ----------------------------- #
class Language(Enum):
    java, python, go, rust = range(1, 5)
    
print(list(Language))


# --------------------------------- Enum auto -------------------------------- #
#* automatically assign value to the enum variable, that start from 1, continue increasing
#* all value will be unique
class Generation(Enum):
    gen1 = auto()
    gen2 = auto()
    gen3 = auto()
    
print(list(Generation))

