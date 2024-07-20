# ---------------------------------------------------------------------------- #
#                                    If else                                   #
# ---------------------------------------------------------------------------- #

num = 10
# ! Be mindful of the indentation while writing the if statements. Indentation is the whitespace at 
# ! the beginning of the code.
print("# --------------------------------- If else --------------------------------- #")

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
    
# ---------------------------------------------------------------------------- #
#                                   For Loop                                   #
# ---------------------------------------------------------------------------- #
print("# --------------------------------- For loop --------------------------------- #")
os_list = ["Linux", "Windows", "Mac"]
for os in os_list:
    print(os)
    
# Iterate through character
langugage = "Systemverilog"
for char in langugage:
    print(char)
    
# For loop with range
for i in range(5):
    print(i)

# * The range() function can also be called with three arguments. The first two
# * arguments will be the start and stop values, and the third will be the step
# * argument
for i in range(10, 20, 2):
    print(i)

for i in range(20, 10, -3):
    print(i)

    
# For loop with else
for i in range(2):
    print(i)
else :
    print("No item left")
    
# Use "_" as placehold and its value is intentionally being ignored.
for _ in range(5):
    print("Execute")

# ---------------------------------------------------------------------------- #
#                                  While Loops                                 #
# ---------------------------------------------------------------------------- #
print("# -------------------------------- While loop -------------------------------- #")

num = 1
while num < 5:
    print(num)
    num = num + 1

# ! Infinite loop with break condition
while True:
    user_input = input("Enter your name: ")
    print("Enter \"end\" to break the while loop")
    if user_input == "end":
        print("This loop has ended")
        break
    print(user_input)

# While loop with else condition
counter = 0
while counter < 5:
    print(counter)
    counter += 1
else :
    print("Counter end")

# ---------------------------------------------------------------------------- #
#                               Break & Conitinue                              #
# ---------------------------------------------------------------------------- #
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# ---------------------------------------------------------------------------- #
#                                     Pass                                     #
# ---------------------------------------------------------------------------- #
# In Python programming, the pass statement is a null statement which can be used 
# as a placeholder for future code.
# * Note: The difference between a comment and a pass statement in Python is that 
# while the interpreter ignores a comment entirely, pass is not ignored.
if num > 10:
    pass

print("Pass")

def foo(args):
    pass
print("Pass")