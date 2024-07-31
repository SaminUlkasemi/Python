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
#* Step for regular expression matching
#   1. Import the regex module with import re.
#   2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
#   3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
#   4. Call the Match object’s group() method to return a string of the actual matched text.


import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
#!search() method will return None if the regex pattern is not found in the string.
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
print(batRegex2.search("The Advantures of Batman").group())
print(batRegex2.search("The Advantures of Batwoman").group())

#* "*"" (called the star or asterisk) means Match “match zero or more”
batRegex3 = re.compile(r'Bat(wo)*man')
print(batRegex3.search("The Advantures of Batman").group())
print(batRegex3.search("The Advantures of Batwowoman").group())
print(batRegex3.search("The Advantures of Batwowowowoman").group())
