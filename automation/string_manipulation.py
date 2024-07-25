# ---------------------------------------------------------------------------- #
#                              String manipulation                             #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners

# ----------------------------- Escape Character ----------------------------- #
# An escape character consists of a backslash (\) followed by the character you want 
# to add to the string
string = 'which are \'islands\' of stars with the \'sea\' of emptiness in between'
print(string)

# -------------------------------- Raw string -------------------------------- #
# Place an "r" before the beginning quotation mark of a string to make it a raw string. 
#* A raw string completely ignores all escape characters and prints any backslash that 
# appears in the string
#* Usefull for regular expression
print(r'which are \'islands\' of stars with the \'sea\' of emptiness in between')

# ----------------------------- Multiline stringx ---------------------------- #
msg = '''Dear Alice,
    Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob'''

print(msg)

# ----------------------------- Multiline Comment ---------------------------- #
'''This is a multiline comment'''

# ------------------------- Index & Slicing a string ------------------------- #
#* slicing a string does not modify the original string.
msg = 'Hello world!'
print(msg[0])
print(msg[4])
print(msg[-1])
print(msg[0:5])
print(msg[:5])
print(msg[6:])
sliced_msg = msg[1:4]
print(sliced_msg)

# -------------------------- in and not in operator -------------------------- #
#! This methods are case sensitive
print("What" in "What is your name")
print("Not" not in "what is you name")

# ------------------------------ String Methods ------------------------------ #
print("------------------------------ String Methods ------------------------------")
# The upper() and lower() string methods return a new string where all the
# letters in the original string have been converted to uppercase or lowercase,
msg = "This is Mustafa"
print(msg.upper())
print(msg.lower())
# The isupper() and islower() methods will return a Boolean True value if the string has at 
# least one letter and all the letters are uppercase or lowercase, respectively
print(msg.islower())
print(msg.isupper())
msg = "assalamu alaikum"
print(msg.islower())

# Chain of methods call
print("kasem".upper().lower().upper())

# ------------------------------------ isX ----------------------------------- #
print(" ------------------------------------ isX ----------------------------------- ")
# isalpha() returns True if the string consists only of letters and is not blank.
print("\"kasem\".isalpha(): ", "kasem".isalpha())
# isalnum() returns True if the string consists only of letters and numbers and is not blank.
print("\"kasem123\".isalpha(): ", "kasem123".isalnum())
# isdecimal() returns True if the string consists only of numeric characters and is not blank.
# isspace() returns True if the string consists only of spaces, tabs, and newlines and is not blank.
# istitle() returns True if the string consists only of words that begin with an uppercase letter followed 
# by only lowercase letters.

#* startwith & endswith useful alternatives to the == equals operator if you need to check only whether 
#* the first or last part of the string, rather than the whole thing, is equal to another string.
print("\"This is Kasem\".startswith(\"This\")", "This is Kasem".startswith("This"))
print("\"This is Kasem\".endswith(\"Kasem\")", "This is Kasem".endswith("Kasem"))

# ------------------------------- join & split ------------------------------- #

joined_str = ' | '.join(['cats', 'rats', 'bats'])
print(joined_str)
joined_str = '  --  '.join(['cats', 'rats', 'bats'])
print(joined_str)


# ? Solve that problem
'''
nums = [3, 43, 76, 71, 76, 13]
nums.sort()
print(str(nums))
joined_str = ' -> '.join([])
print(joined_str)
'''

#* By default, split works wherever whitespace characters such as the space, tab, or newline characters
text1 = "A rich cluster of galaxies in the constellation Fornax, showing a variety of structural types."
print(text1.split())

# split with delimeter
text2 = "M. Lipp, M. T. Aga, M. Schwarz, D. Gruss, C. Maurice, L. Raab, and L. Lamster, “Nethammer: Inducing \
Rowhammer faults through network requests,” arXiv preprint arXiv:1805.04956, 2018."
print(text2.split(','))

print("Welcome".rjust(20, "-"))
print("Welcome".ljust(20, '-'))
print("Welcome".center(20, '-'))

print("Picnic item".center(50, '-'))
print("Sandwiches".ljust(20, '-') + "120".rjust(10, '-'))
print("Apple".ljust(20, '-') + "70".rjust(10, '-'))
print("Guava".ljust(20, '-') + "5".rjust(10, '-'))

# ---------------------------- Removing Whitespace --------------------------- #
text = "        Welcome      "
print(text.strip())
print(text.rstrip())
print(text.lstrip())

text = "IntroIntroNewIntroductionIntroIntro"
print(text.strip("Intro"))


# --------------------------------- pyperclip -------------------------------- #