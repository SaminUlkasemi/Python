############################## If else #############################

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

# Multiple condition
if num > 5 and num < 15:
    print("Num greater than 5 less than 15")
    
    
    
############################## Loops #############################
os_list = ["Linux", "Windows", "Mac"]
for os in os_list:
    print(os)
    
langugage = "Systemverilog"
for char in langugage:
    print(char)
    

# For loop range
for i in range(5):
    print(i)
    
# For loop with else
for i in range(2):
    print(i)
else :
    print("No item left")
    
# Usse "_" as placehold and its value is intentionally being ignored.
for _ in range(5):
    print("Execute")
    
