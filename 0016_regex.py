#===========================================================================
#  ?                                ABOUT
#  @author         :  Sazin Reshed Samin
#  @email          :  sazin.reshed.samin@ulkasemi.com
#  @repo           :  SaminUlkasemi
#  @createdOn      :  
#  @description    :  
#===========================================================================

# ---------------------------------------------------------------------------- #
#                          Pattern Matching with Regex                         #
# ---------------------------------------------------------------------------- #

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
number = phoneNumRegex.search('My number is 234-543-232')
print("Phone number found: ", number.group())
# In one line
print("Car number found: ", re.compile(r'\d\d-\d\d\d').search("Car numer 12-344").group())

#* Putting parenthesis will create group,
#* using .ground(group number) method we can put group number to access the group
#! group number start from 1 not 0, putting 0 or noting will return the entire matched text
carNumberRegex = re.compile(r'(\d\d)-(\d\d\d\d)')
carNumber = carNumberRegex.search("Car number is 13-5656")
print("vehicle zone: ", carNumber.group(1))
print("vehicle registration: ", carNumber.group(2))

#* Retrieve the all groups at once
print(carNumber.groups())


phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d\d)')
mo = phoneNumRegex.search('Phone number is (233) 3432')
print(mo.groups())
