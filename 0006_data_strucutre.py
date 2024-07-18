# ---------------------------------------------------------------------------- #
#                                     List                                     #
# ---------------------------------------------------------------------------- #
""" List Characteristics :
Ordered - They maintain the order of elements.
Mutable - Items can be changed after creation.
Allow duplicates - They can contain duplicate values. """
print("# ----------------------------------- List ----------------------------------- #")

arr = ["Apple", 10.2, 4, 2+4j, True]
for i in arr:
    print(i)

 # Emppty list
arr = []
print(arr)
# Using list to create list 
lang = "Python"
lang_list = list(lang)
print(lang_list)
# Negative indexing
print(lang_list[-1])
# Slicing a list
print(lang_list[2:4])

# -------------------------------- List Length ------------------------------- #
print("list length:", len(arr))


# -------------------------------- List Method ------------------------------- #
# Append
arr = ["Apple", "Orange", "Pineapple", "Watermelon"]

arr.append("Mango")
print(arr)

# Add to specifiq index
arr.insert(1, "Banana")
print(arr)

# Change list item
arr[2] = "Jackfruit"
print(arr)

# Remove item by name
arr.remove("Banana")
print(arr)

# Remove one or more element
del arr[2]
print(arr)

del arr[1:4]
print(arr)

# ---------------------------- List Comprehension ---------------------------- #
numbers = [n / 2 for n in range(5)]
print(numbers)


# ---------------------------------------------------------------------------- #
#                                     Tuple                                    #
# ---------------------------------------------------------------------------- #
# * A tuple is a collection similar to a Python list. The primary difference is that 
# ! we cannot modify a tuple once it is created.
# Tuple Characteristics
# Ordered - They maintain the order of elements.
# Immutable - They cannot be changed after creation.
# Allow duplicates - They can contain duplicate values.
print("# ----------------------------------- Tuple ---------------------------------- #")

number = (1, 2, 3)
print(number)

# ! Altering the tuple item will throw error
#   <module>
#     number[2] = 33
#     ~~~~~~^^^
#  TypeError: 'tuple' object does not support item assignment
# number[2] = 33 

# ----------------------- Create a tuple with one item ----------------------- #
var = ('Python')
# ! Declearing tuple with one item will make string instead of tuple
for v in var:
    print(v)

# * So we need to add trainling comma after the tuple item
var = ("Python",)
for v in var:
    print(v)

# ---------------------------------------------------------------------------- #
#                                      Set                                     #
# ---------------------------------------------------------------------------- #
# * A set is a collection of unique data, meaning that elements within a set 
# * cannot be duplicated
# A set can have any number of items and they may be of different types (integer, float, tuple, string, etc.). 
# !But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
print("------------------------------------ Set ----------------------------------- ")

student_id = {22, 4, 56, 2}
student_id.add(22) # Output {56, 2, 4, 22}
# Adding same element that already contain in set will not added in the set
print(student_id)
# ! Set output may be in a different order. This is because the set has no particular order.

# Creating an empty set is a bit tricky. #! Empty curly braces {} will make an empty dictionary in Python.
my_set_1 = {}
# To make a set without any elements, we use the set() function without any argument. For example,
my_set_2 = set()

print(type(my_set_1))
print(type(my_set_2))

# ! since they are unordered, indexing has no meaning. We cannot access or change an element 
# ! of a set using indexing or slicing. The set data type does not support it.
# -------------------------------- Set Method -------------------------------- #
# Add item in set
student_id.add(15)
print(student_id)
# Update item in set
my_list = [1, 2, 3, 4]
student_id.update(my_list)
print(student_id)
# Remove element from set
student_id.discard(22)
print(student_id)

