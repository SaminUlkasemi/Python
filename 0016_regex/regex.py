#===========================================================================
#  ?                                ABOUT
#  @author         :  Sazin Reshed Samin
#  @email          :  sazin.reshed.samin@ulkasemi.com
#  @repo           :  SaminUlkasemi/Python
#  @createdOn      :  
#  @description    :  
#===========================================================================

# ---------------------------------------------------------------------------- #
#                          Pattern Matching with Regex                         #
# ---------------------------------------------------------------------------- #
#*  Python has two ways for regular expresssion
#   1 ---->
#       I.   Import the regex module with import re.
#       II.  use re.search(regex, text)
#       III. use .group() result string
#   2 ---->
#       I.   Import the regex module with import re.
#       II.  Create a Regex object with the re.compile() function. (Remember to use a raw string.)
#       III. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
#       IV.  Call the Match object’s group() method to return a string of the actual matched text.

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
#! search() method return None if the regex pattern is not found in the string.
#! search() method return Match object not string
number = phoneNumRegex.search('My number is 234-543-232')
print("Phone number found: ", number.group())
# In one line
print("Car number found: ", re.compile(r'\d\d-\d\d\d').search("Car numer 12-344").group())


# -------------------------------- RegEx group ------------------------------- #
#* Putting parenthesis will create group,
#* using .ground(group number) method we can put group number to access the group
#! group number start from 1 not 0, putting 0 or noting will return the entire matched text
carNumberRegex = re.compile(r'(\d\d)-(\d\d\d\d)')
carNumber = carNumberRegex.search("Car number is 13-5656")
print("vehicle zone(group 1): ", carNumber.group(1))
print("vehicle registration(group 2): ", carNumber.group(2))

#* Retrieve the all groups at once
print("carNumber.groups(): ", carNumber.groups())

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d\d)')
mo = phoneNumRegex.search('Phone number is (233) 3432')
print(mo.groups())


# ------------------ Matching Multiple Groups with the Pipe ------------------ #
print("Matching Multiple Groups with the Pipe".center(70, '-'))

# for multiple matching using pipe first occurrence of matching text will be returned
pipeRegex = re.compile(r'vscode|python')
mo = pipeRegex.search('I am using vscode for python coding')
print(mo.group())

pipeRegex = re.compile(r'vscode|python')
mo = pipeRegex.search('I do python coding using vscode')
print(mo.group())

# use the pipe to match one of several patterns as part of your regex.
barRegex =  re.compile(r'Bat(man|mobile|copter|bat)')
mo = barRegex.search('Batcopter lost a wheel')
print(mo.group())
print(mo.group(1))


# ----------------- Optional Matching with the Question Mark ----------------- #
#* "?" indicate Match "zero or one" of the group preceding this question mark
batRegex2 = re.compile(r'Bat(wo)?man')
print("Bat(wo)?man: ", batRegex2.search("The Advantures of Batman").group())
print("Bat(wo)?man: ", batRegex2.search("The Advantures of Batwoman").group())

#* "*"" (called the star or asterisk) means Match “match zero or more”
batRegex3 = re.compile(r'Bat(wo)*man')
print("Bat(wo)*man: ", batRegex3.search("The Advantures of Batman").group())
print("Bat(wo)*man: ", batRegex3.search("The Advantures of Batwowoman").group())
print("Bat(wo)*man: ", batRegex3.search("The Advantures of Batwowowowoman").group())

#* "+" Match one or more
print("Bat(wo)+man: ", re.search(r'Bat(wo)+man', "The Advantures of Batwowoman").group())
res = re.search(r'Bat(wo)+man', "The Advantures of Batman")
print(res)

# --------------------------- Specific Repetitions --------------------------- #
print("Specific Repetitions".center(70, '-'))
print("ha{2, 5}: ", re.search(r'(ha){2,5}', "hahahaha").group())

# ---------------------------- Greedy & Non-Greedy --------------------------- #
#* Greey     -> return alawys the longest matched string
#* Non-Greey -> return alawys the longest matched string
# Python regex by default Greedy
print("Greedy matching     -> ha{2, 5}: ", re.search(r'(ha){2,5}', "hahahaha").group())
print("Non-Greedy matching -> ha{2, 5}: ", re.search(r'(ha){2,5}?', "hahahaha").group())

#! Note that the question mark can have two meanings in regular expressions: 
#! declaring a nongreedy match or flagging an optional group. 

# ---------------------------------- findall --------------------------------- #
#  findall() method will return the strings of every match in the searched string
print("56455634355676556: ", re.findall("56", "56455634355676556"))
# If there are groups in the regular expression, then findall() will return a list of tuples
print("Cell: 415-555-9999 Work: 212-555-0000: ", re.findall(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)', \
    "Cell: 415-555-9999 Work: 212-555-0000"))

# ----------------------------- Character Classes ---------------------------- #
print("Character class".center(70, '-'))
print(re.findall(r'\d+\s\w+', "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
                        swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'"))

# Making Your Own Character Classes
print("[aeiouAEIOU]: ", re.findall(r'[aeiouAEIOU]', "RoboCop eats baby food. BABY FOOD."))

#* inside the square brackets, the normal regular expression symbols are
#* not interpreted as such. This means you do not need to escape the ., *, ?, or ()
#* characters with a preceding backslash

# ranges of letters or numbers
print("[a-e]: ", re.findall(r'[a-e]', 'The sun rose early that morning, \
                                        casting a golden glow over the horizon'))

# caret character (^) A negative character class will match all the characters that 
# are not in the character class.
print("[^a-e]: ", re.findall(r'[^a-e]', 'The sun rose early that morning, \
                                        casting a golden glow over the horizon'))

# caret symbol (^) at the start of a regex to indicate that a match must occur 
# at the beginning of the searched text
print(re.search(r'^The', "The sun has set already").group())

# dollar sign ($) at the end of the regex to indicate the string must end with this
# regex pattern
print(re.search(r'\d$', "My roll is 3").group())

# ---------------------------- Wildcard Character ---------------------------- #
print("Wildcard Character".center(70, '-'))

# .(dot) -> match any character except for a newline
#* Remember that the dot character will match just one character
print(".at", re.findall(r'.at', "The cat in the hat sat on the flat mat."))

# .* (dot start) -> want to match everything and anything
mo = re.search(r'First Name: (.*) Last Name: (.*)', "First Name: Hasan Last Name: Ahmed")
print(mo.group(1))
print(mo.group(2))

# greedy
print("     greedy: ", re.search(r'<.*>', "<To serve man> for dinner.>").group())
# non-greedy
print("Non- greedy: ", re.search(r'<.*?>', "<To serve man> for dinner.>").group())