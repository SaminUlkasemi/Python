# https://www.programiz.com/python-programming/operators
#####################   Arithmatic  #####################
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
print("num1 ** num2: ", num1**num2)


####################    Logical ##########################
print("(num1 > num2) and (num2 < num1): ", (num1 > num2) and (num2 < num1))
print("(num1 > num2) or  (num2 > num1): ", (num1 > num2) or  (num2 > num1))
print("not num1 > 20:", not num1 > 20)


####################    Bitwise ##########################
bits1 = 0b010101
bits2 = 0b101010

print("bits1 & bits2: {:b}".format(bits1 & bits2))
print("bits1 | bits2: {:b}".format(bits1 | bits2))