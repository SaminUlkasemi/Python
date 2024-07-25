
# ---------------------------------------------------------------------------- #
#                                   variable                                   #
# ---------------------------------------------------------------------------- #
site_name = "programiz"
print(site_name)

# * Python is a type-inferred language, so you don't have to explicitly define the variable type.
# * It automatically knows that programiz.pro is a string and declares the site_name variable
# * as a string.
# * Variable names are case-sensitive(meaning that spam, SPAM, Spam, and sPaM are
# * four different variables)

# Integer
var_int = 10
# Float
var_float = 10.2
# Character
character = 's'
# Boolean
is_pass = True
# Special(null)
special_var = None
# Complex number
complex_num = 2 + 3j

print(var_int, var_float, character, is_pass, special_var)


# Number System	    Prefix
# Binary	        0b or 0B
# Octal	            0o or 0O
# Hexadecimal	    0x or 0X


# Assigning multiple values to multiple variables
a, b, c = 3, 10.2, "Linux"
print(a, b, c)

# Assign the same value to multiple variables at once
name1 = name2 = "Windows"
print(name1, name2)


# Know type in python
print(type(var_int))
print(type(var_float))
print(type(character))
print(type(is_pass))
print(type(special_var))
print(type(complex_num))

# ---------------------------------------------------------------------------- #
#                              Python Type Casting                             #
# ---------------------------------------------------------------------------- #
int_num     = 10
float_num   = 10.2

# ----------------------------- Implicit Casting ----------------------------- #
# Python always converts smaller data types to larger data types to avoid the 
# loss of data.
result1 = int_num + float_num
print("result1", result1)

# ------------------------------ Explict Casting ----------------------------- #
num_string  =  "12"
result2     =   float_num + int(num_string)
print("result2", result2) 

result3 = num_string + str(float_num)
print("result3", result3)