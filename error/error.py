# ---------------------------------------------------------------------------- #
#                                AttributeError                                #
# ---------------------------------------------------------------------------- #
#! If a method belong to list & If we use that method in string or integer then 
#! AttributeError message will be thrown
var = "Python"
var.append("Java") 

# ---------------------------------------------------------------------------- #
#                                  ImportError                                 #
# ---------------------------------------------------------------------------- #
# Error: 
#!   ImportError: cannot import name 'ArgumentParser' from partially initialized module 'argparse' 
#!   (most likely due to a circular import) (/home/samin/Videos/Python/command_line_argument/argparse.py
# Solve:
#*   Don't give same file name which match with Python module or file name
#   Links: https://stackoverflow.com/a/66055075/10928027


# ---------------------------------------------------------------------------- #
#                                  ValueError                                  #
# ---------------------------------------------------------------------------- #
#!  ValueError: Row numbers must be between 1 and 1048576. Row number supplied was 0
# Solve:
#*      When working with excel sheet row number should be between 1 to 1048576