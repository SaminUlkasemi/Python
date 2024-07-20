# https://www.programiz.com/python-programming/operators
# ---------------------------------------------------------------------------- #
#                              Arithmatic Operator                             #
# ---------------------------------------------------------------------------- #
num1 = 10
num2 = 5.5

# Addition
print("num1 + num2 : ", num1 + num2)
# Substraction
print("num1 - num2 : ", num1 - num2)
# Division
print("num1 / num2 : ", num1 / num2)
# Floor division
print("num1 // num2: ", num1 // num2)
# Module
print("num1 % num2 : ", num1 % num2)
# Power
print("num1 ** num2: ", num1 **num2)

# ---------------------------------------------------------------------------- #
#                                    Logical                                   #
# ---------------------------------------------------------------------------- #
print("(num1 > num2) and (num2 < num1): ", (num1 > num2) and (num2 < num1))
print("(num1 > num2) or  (num2 > num1): ", (num1 > num2) or  (num2 > num1))
print("not num1 > 20:", not num1 > 20)

# ---------------------------------------------------------------------------- #
#                                    Bitwise                                   #
# ---------------------------------------------------------------------------- #
bits1 = 0b010101
bits2 = 0b101010
bits3 = 0b111111

print("bits1 & bits2: {:b}"  .format(bits1 & bits2))
print("bits1 | bits2: {:b}"  .format(bits1 | bits2))
print("~bits3       : {:b}"  .format(~bits3));
print("bits1 ^ bits2: {:b}"  .format(bits1 ^ bits2))
print("bits1 << 2   : {:06b}".format(bits3 << 2))
print("bits1 >> 2   : {:06b}".format(bits3 >> 2))

# ---------------------------------------------------------------------------- #
#                               Identity Operator                              #
# ---------------------------------------------------------------------------- #
# In Python, is and is not are used to check if two values are located at the same memory location.
x1 = 10
x2 = 10
x3 = 20
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("x1 is x2: "     , x1 is x2)
print("x1 is not x3: " , x1 is not x3)
print("list1 is list2:", list1 is list2)

# ---------------------------------------------------------------------------- #
#                                  Membership                                  #
# ---------------------------------------------------------------------------- #
print(2 in list)