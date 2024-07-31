# ---------------------------------------------------------------------------- #
#                                 File Handling                                #
# ---------------------------------------------------------------------------- #
# Ref: Automate the Boring Stuff with Python_ Practical Programming for Total Beginners
# Chapter: 8
# with open ref: https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/

# ------------------------------- Filename Path ------------------------------ #
import os
print(os.path.join("usr", "bin", "bash"))

# ------------------------- Current Working Directory ------------------------ #
# Get current directory
print("current dir:", os.getcwd())
# Change current directory
print(os.chdir('garbage'))
print("current dir:", os.getcwd())

#! Python will display an error if you try to change to a directory that does not exist.

# --------------------------- Creating New Folders --------------------------- #
print("Creating new directory".center(70, '-'))
try:
    os.makedirs('../garbase/gasbase_f1/garbase_inside')
except:
    print("Folder already exits") 

# ------------------------ Absolute & Relative folder ------------------------ #
#* An absolute path, which always begins with the root folder
#* A relative path, which is relative to the program’s current working directory
print("Absolute & Relative path".center(70, '-'))

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
print("File Size & Folder contents".center(70, '-'))
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
print('Documents folder'.center(70, "-"))
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
print("Checking path validity".center(70, "-"))
try:
    print(os.path.exists(r"C:\Users\230907\Documents"))
    # print(os.path.exists("/home/samin/Documents"))
except Exception as e:
    print(e)

# --------------------- Find only specifiq types of file --------------------- #
print("Find only specifiq types of file".center(70, "-"))
print("Current dir: ", os.getcwd())

for fileName in os.listdir('.'):
    if not fileName.endswith('txt'):
        continue
    else:
        print(fileName)
        
# ---------------------------------------------------------------------------- #
#                               Organizing Files                               #
# ---------------------------------------------------------------------------- #
print("Organizing files & Folder".center(70, '-'))
import shutil

os.chdir('../0011_file_handling/file')
#* shutil.copy copy files & shutil.copytree() copy the entire folder recursively
#* These functions return a string of the absolute path of the new location.
# -------------------------------- Copy a file ------------------------------- #
try:
    print(shutil.copy('folders/text1.txt', 'dir/myText1.txt'))
except Exception as e:
    print(e)
    
# ----------------------- Copy a directory recursively ----------------------- #
try:
    print(shutil.copytree('folders', 'dir/copied_dir'))
except Exception as e:
    print(e)
    
# --------------------- Moving & Renaming Files & Folders -------------------- #
#* If destination points to a folder, the source file gets moved into destination
#* and keeps its current filename. 
#! If there had been a bacon.txt file already in C:\eggs, it would have been overwritten.
try:
    shutil.move('text_for_move.txt', 'moved_dir')
except Exception as e:
    print(f'Files already moved: {e}')
    
#* The destination path can also specify a filename.
#* In this case the source file is moved and renamed
try:
    shutil.move("text_for_moving_2.txt", 'moved_dir/move2.txt')
except Exception as e:
    print(e)
    
#! If given destination folder doesn't exits, 
#! then move() will rename source files name as destination files name
#! means there is not .txt extension in the file
try:
    shutil.move("file_for_move3.txt", 'myfile')
except Exception as e:
    print(e)
    
# ------------------ Permanently Deleting Files and Folders ------------------ #
#  os.unlink(path)
#  os.rmdir(path) 
#  For Safe Deletes use third-party send2trash Module

# ------------------------- Walking a directory tree ------------------------- #
print(os.getcwd())
for folderNames, subFolders, fileNames in os.walk("."):
    print("Folder")
    print(folderNames)
    print(" - Subfolder: ")
    for subFolder in subFolders:
        print(f"    {subFolder}")
    print(" - Filenames")
    for fileName in fileNames:
        print(f"    {fileName}")