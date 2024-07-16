num = 10
#  Be mindful of the indentation while writing the if statements. Indentation is the whitespace at 
#  the beginning of the code.
if num > 10:
    print("Num greater than 5")
elif num < 15:
    print("Num less than 5")
else :
    print("None")
    
if num > 5 :
    if num > 7:
        print("Num greater than 7")
    else :
        print("Num less than 7")
else :
    print("Num less than 5")

# shorthand
if num > 5 : print("Num greater than 5")

# Ternary if else
grade = 83
resut = "pass" if grade > 55 else "fail"
print(resut)

if num > 5 and num < 15:
    print("Num greater than 5 less than 15")