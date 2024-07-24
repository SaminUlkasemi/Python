# ---------------------------------------------------------------------------- #
#                            Reading & Writing File                            #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners
# Chapter: 8

# ------------------------------- Filename Path ------------------------------ #
import os
print(os.path.join("usr", "bin", "bash"))

# ------------------------- Current Working Directory ------------------------ #
# Get current directory
print("current dir:", os.getcwd())
# Change current directory
print(os.chdir('garbase'))
print("current dir:", os.getcwd())

#! Python will display an error if you try to change to a directory that does not exist.

# --------------------------- Creating New Folders --------------------------- #
print("Creating new directory".center(70, '*'))
try:
    os.makedirs('../garbase/gasbase_f1/garbase_inside')
except:
    print("Folder already exits") 

# ------------------------ Absolute & Relative folder ------------------------ #
#* An absolute path, which always begins with the root folder
#* A relative path, which is relative to the program’s current working directory
print("Absolute & Relative path".center(70, '*'))

# os.path.abspath(path) will return a string of the absolute path
try:
    print(os.path.abspath("garbase"))
except:
    print("Dir not found")
# os.path.isabs(path) will return True if the argument is an absolute path
try:
    print(os.path.isabs("garbase"))
except:
    print("Dir not found")
#? os.path.relpath(path, start) will return a string of a relative path from the start path to path. 
#* If start is not provided, the current working directory is used as the start path
try:
    print(os.path.relpath("garbase_f1", "/"))
except:
    print("Dir not found")

print(os.path.dirname("home/samin/Videos/Python/garbase"))
print(os.path.basename("home/samin/Videos/Python/garbase"))

# ------------------------ File Size & Folder contents ----------------------- #
print("File Size & Folder contents".center(70, '*'))
# os.path.getsize(path) will return the size in bytes of the file
try:
    print(os.path.getsize('/home/samin/Downloads'))
except:
    print("Dir not found")

# os.listdir(path) will return a list of filename
try:
    print(os.listdir('/home/samin/Documents'))
except:
    print("Dir not found")

print('Documents folder'.center(70, "*"))
filesSize = {}
for filename in os.listdir('/home/samin/Documents'):
    filesSize[filename] = os.path.getsize('/home/samin/Documents/' + filename)

print("Name".ljust(70), "Size", "\n")
for k, v in filesSize.items():
    print(str(k).ljust(70, '-'), str(v).ljust(1))