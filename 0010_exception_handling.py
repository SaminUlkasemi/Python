# ---------------------------------------------------------------------------- #
#                              Exception Handling                              #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners
# Ref: finally -> https://www.w3schools.com/python/ref_keyword_finally.asp, 
#              -> https://www.geeksforgeeks.org/finally-keyword-in-python/        
#              -> https://www.geeksforgeeks.org/try-except-else-and-finally-in-python/       
# Ref: custom exception -> https://www.programiz.com/python-programming/user-defined-exception
# Ref: https://docs.python.org/3/tutorial/errors.html

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

# Print the exception
try:
    print(10/0)
except Exception as e:
    print(f"Error: {e}")
    
# ---------------------------------- Finally --------------------------------- #
print("Finally".center(70, "-"))
#* The finally block will always be executed, no matter if the try block raises an error or not
# Uses: there may be some situation in which the current method ends up while handling some exceptions. 
# But the method may require some additional steps before its termination, like closing a file or a network and so on
try:
    x = 10 / 0
except Exception as e:
    print(e)
finally:
    print("The try..except block has finished")

# ------------------------ try, except, else, finally ------------------------ #
try:
    res = 10 / 2
except Exception as e:
    print(e)
else:
    print(f"result: {res}")
    
    
# ----------------------------- Custome Exception ---------------------------- #
print("Custom Exception".center(70, '-'))
class InvalidAgeException(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeException
    else:
        print("Eligible for driving")
except InvalidAgeException:
    print("Invalid age")
    

class SalaryRangeException(Exception):
    
    def __init__(self, salary, message="Salary must be inside 50-100"):
        self.salary     = salary
        self.message    = message
        super().__init__(self.salary, self.message)

salary = int(input("Enter your salary: "))
if salary < 10 or salary > 100:
    raise SalaryRangeException(salary)
