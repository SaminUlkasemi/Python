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