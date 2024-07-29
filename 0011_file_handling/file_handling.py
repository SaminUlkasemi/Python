# ---------------------------------------------------------------------------- #
#                                 File Handling                                #
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

# ------------------- Function to get the files & it's size ------------------ #
print('Documents folder'.center(70, "*"))
filesSize = {}
try:
    for filename in os.listdir('/home/samin/Documents'):
        filesSize[filename] = os.path.getsize('/home/samin/Documents/' + filename)

    print("Name".ljust(70), "Size", "\n")
    for k, v in filesSize.items():
        print(str(k).ljust(70, '-'), str(v).ljust(1))
except:
    print("Dir not found")
    
# ! This portion works only in windows
# -------------------------- Checking path validity -------------------------- #
print("Checking path validity".center(70, "*"))
try:
    # print(os.path.exists(r"C:\Users\230907\Documents"))
    print(os.path.exists("/home/samin/Documents"))
except Exception as e:
    print(e)

# ------------------------------ Opening a file ------------------------------ #
print("Opening a file".center(70, "*"))

# The open() function returns a File object. Read mode is the default mode for files. We can 
#* explicitly specify the mode by passing the string value 'r' as a second argument
try:
    file = open("/home/samin/Videos/Python/garbase/myFile.txt")
except Exception as e:
    print(f"Failed to open the file: {e}")

# ------------------------------ Reading a file ------------------------------ #
fileContent = file.read()
print(fileContent)

# readlines() method to get a list of string values from the file, one string for each line of text
# ? Won't work
line_list = file.readlines()
print(line_list)

# ------------------------ Writing or Appending a File ----------------------- #
#! You can’t write to a file you’ve opened in read mode

#* Write mode will overwrite the existing file and start from scratch
# This method returns the number of characters written, including the newline
# write() method does not automatically add a newline character to the end of the string
fileForWrite = open("/home/samin/Videos/Python/garbase/myFile2.txt", 'w')
fileForWrite.write("Name: Hasan\n")
#! After reading or writing a file, call the close() method before opening the file again.
fileForWrite.close()

#* Append mode, on the other hand, will append text to the end of the existing file.
fileForAppend = open("/home/samin/Videos/Python/garbase/myFile2.txt", 'a')
fileForAppend.write('ID: 23213')
fileForAppend.close()