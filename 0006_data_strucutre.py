# ---------------------------------------------------------------------------- #
#                                     List                                     #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners

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
print("lang_list:", lang_list)
# Negative indexing
print("lang_list[-1]:", lang_list[-1])
# Slicing a list
print("lang_list[2:4]: ", lang_list[2:4])
# Slicing list with negative index
print("lang_list[0:-2]:", lang_list[0:-2])
# Slicing shorcut
print("lang_list[:2]:", lang_list[:2])
print("lang_list[2:]:", lang_list[:2])

# ------------------------------ Nester array ------------------------------ #
arr = [[[34, 34], [34, 45], [[12, 76], [84, 983, 45]]]]
# Access nester array
print("arr[0][1][1]:", arr[0][1][1])

# -------------------------------- List Method ------------------------------- #
# List length
print("list length:", len(arr))

# Append
arr = ["Apple", "Orange", "Pineapple", "Watermelon"]

arr.append("Mango")
print(arr)

# Add to specifiq index
arr.insert(1, "Banana")
print(arr)

#! Neither append() nor insert() gives the new value of spam as its return value. 
#*(In fact, the return value of append() and insert() is None, so you definitely 
#* wouldn’t want to store this as the new variable value.) Rather, the list is modified in place.

# Change list item
arr[2] = "Jackfruit"
print(arr)

# Remove item by name
#* value appears multiple times in the list, only the first instance of the value will be removed.
arr.remove("Banana") #! Attempting to delete a value that does not exist in the list will result in a ValueError error
print(arr)

# Remove one or more element
del arr[2]
print(arr)

del arr[1:4]
print(arr)

#*  The del statement is good to use when you know the index of the value you want to remove from the list. 
#* The remove() method is good when you know the value you want to remove from the list.

print(arr.index('Apple')) #! If the value isn’t in the list,then Python produces a ValueError error
# * If the value isn’t in the list, then Python produces a ValueError error

# ---------------------- List concatation & Replication ---------------------- #
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Concatanation: list1 + list2: ", list1 + list2)
print("Replication list1 * 2:", list1 * 2)


# ---------------------------- List Comprehension ---------------------------- #
numbers = [n / 2 for n in range(5)]
print(numbers)

# ------------------------------- List looping ------------------------------- #
print("# ------------------------------- List looping ------------------------------- #")
list = [23, 34, 3, 4, 34, 2, 34, 23, 4]
for i in range(len(list)) :
    print("list["+str(i)+"]:", list[i])


# ------------------------ The in and not in Operators ----------------------- #
animals = ["cat", "dog", "elephant"]
print("dog in animals: ", "dog" in animals)
print("cat not in animals: ", "cat" not in animals)

# ----------------------- The Multiple Assignment Trick ---------------------- #
# ! The number of variables and the length of the list must be exactly equal, 
# ! or Python will give you a ValueError:
cat, dog, elephant = animals
print(cat, dog, elephant)

# ---------------------- Augmented Assignment Operators ---------------------- #
animals *= 2
print(animals)

# ---------------------------------- Sorting --------------------------------- #
#* sort() method sorts the list in place
#* you cannot sort lists that have both number values and string values
#* sort() uses “ASCIIbetical order"
print("# ---------------------------------- Sorting --------------------------------- #")

num_list = [23, 45, 12, 4, 5]
num_list.sort()
print(num_list)

# Reverse sort
num_list.sort(reverse=True)
print(num_list)

# Alphabetical sort
alphabet_list = ['A', 'b', 'C', 'z']
# ! Problem
alphabet_list.sort(key=str.lower)
print(alphabet_list)
# ! Problem
alphabet_list.sort(key=str.upper)
print(alphabet_list)


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

#* (Unlike some other programming languages, in Python it’s fine to have a trailing comma after 
#* the last item in a list or tuple

#* because they are immutable and their contents don’t change, Python can implement some optimizations 
#* that make code using tuples slightly faster than code using lists.

# ------------------------- Converting list to tuple ------------------------- #
my_list = [23, 34, 4]
my_tuple = tuple(my_list)
print(my_tuple)

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

# ---------------------------------------------------------------------------- #
#                                  Dictonaries                                 #
# ---------------------------------------------------------------------------- #
#* Indexes for dictionaries are called keys, and a key with its associated value is
#* called a key-value pair.
print("---------------------------- Dictonaries -------------------------------")
myCat = {'size' : 'small', 'color' : 'orange', 'disposition' : 'loud'}

# ---------------------------- List VS Dictonaries ---------------------------- #
# While the order of items matters for determining whether two lists are the same, it does not
# matter in what order the key-value pairs are typed in a dictionary
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

#! Because dictionaries are not ordered, they can’t be sliced like lists.

# ---------------------------- Dictonaries Methods ---------------------------- #
#* The .key(), .values(), .item() methods return list-like values, 
#! they are not true list, They cannot be modified and do not have an append() method
#* hese data types (dict_keys, dict_values, and dict_items, respectively) can be used in for loops.

print("Keys")
for i in myCat.keys():
    print(i)

print("values")
for i in myCat.values():
    print(i)

print("items")
for i in myCat.items():
    print(i)

# get() method that takes two arguments: the key of the value to retrieve and a fallback value to 
# return if that key does not exist.
picnitItem = {'apple': 5, 'eggs': 10}
print("I am bringing", picnitItem.get("apple", 0),  "for the picnic")
print("I am bringin",  picnitItem.get("orange", 0), "for the picnic") # Because there is no 'orange' key 
# in the picnicItem dictionary, the default value 0 is returned by the get() method.

# In setdefault() method first argument passed to the method is the key to check for, and 
# the second argument is the value to set at that key if the key does not exist. If the key 
# does exist, the setdefault() method returns the key’s value.
myCar = {'cc' : 2000, 'type' : 'SUV'}
print(myCar.setdefault('color', 'black'))
print(myCar.setdefault('color', 'blue'))

myBike = {'engine' : {'cc': 165, 'stroke': 4}, 'color': 'blue'}
# use pprint for nice display of dictonaries value
import pprint
pprint.pprint(myBike)


# ---------------------------- Mutiple assignment ---------------------------- #
for k, v in myCat.items():
    print("Key:", k, ",", "Value: ", v)

# ---------- Checking Whether a Key or Value Exists in a Dictionary ---------- #
print('cat' in eggs.values())
print('age' not in eggs.keys())

