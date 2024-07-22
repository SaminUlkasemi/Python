# ---------------------------------------------------------------------------- #
#                                  References                                  #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners

#* When you assign a list to a variable, you are actually assigning a list reference
#* to the variable. A reference is a value that points to some bit of data.

my_list_1 = ['Apple', 'Mango', 'Banana']
my_list_2 = my_list_1       # Instead of value the list reference is conpied
my_list_2[1] = "Orange"     #! Now changing one list item will change the another list as well

print("my_list_1: ",my_list_1)
print("my_list_2: ",my_list_2)

# Variables will contain references to list values rather than list values themselves.
# But for strings and integer values, variables simply contain the string or integer
#* value. Python uses references whenever variables must store values of mutable
#* data types, such as lists or dictionaries. For values of immutable data types such
#* as strings, integers, or tuples, Python variables will store the value itself.

# ---------------------------- Passing references ---------------------------- #
#* When a function is called, the values of the arguments are copied to the parameter 
#* variables. For lists , this means a copy of the reference is used for the parameter.

my_list_3 = [12, 12, 12]
def appenedList(my_list):
    my_list.append(11)

appenedList(my_list_3)
print(my_list_3)

# ------------------------------ copy() & deepCopy() ----------------------------- #
import copy

animalList1 = ['Dog', 'Cat', 'Tiger']
#* copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary, 
#* not just a copy of a reference.
animalList2 = copy.copy(animalList1)

animalList2[1] = 'Lion'

print("animalList1:", animalList1)
print("animalList2:", animalList2)

# The deepcopy() function will copy these inner lists as well.
list_1 = [[1, 2, 3], [4, 5, 6]]
list_2 = copy.deepcopy(list_1)

list_2[0][1] = 200

print("list_1: ", list_1)
print("list_2: ", list_2)