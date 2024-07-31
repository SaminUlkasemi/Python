# ---------------------------------------------------------------------------- #
#                                 Text handling                                #
# ---------------------------------------------------------------------------- #
import os
print("Current dir: ", os.chdir('0011_file_handling/text'))

# ------------------------------ Opening a file ------------------------------ #
print("Opening a file".center(70, "-"))

# The open() function returns a File object. Read mode is the default mode for files. We can 
#* explicitly specify the mode by passing the string value 'r' as a second argument
try:
    file = open("myFile.txt")
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
print("Write & Append".center(70, '-'))
#! You can’t write to a file you’ve opened in read mode

#* Write mode will overwrite the existing file and start from scratch
# This method returns the number of characters written, including the newline
# write() method does not automatically add a newline character to the end of the string
fileForWrite = open("myFile2.txt", 'w')
fileForWrite.write("Name: Hasan\n")
#! After reading or writing a file, call the close() method before opening the file again.
fileForWrite.close()

#* Append mode, on the other hand, will append text to the end of the existing file.
fileForAppend = open("myFile2.txt", 'a')
fileForAppend.write('ID: 23213')
fileForAppend.close()

# --------------------------------- with open -------------------------------- #
print("with open".center(70, '-'))
print("Current directory: ", os.getcwd())
#* Unlike open() where you have to close the file with the close() method, the with statement closes
# the file for you without you telling it to.
#* This is because the with statement calls 2 built-in methods behind the scene – __enter()__ and __exit()__.
#? --- this below don't work 
try:
    with open("myFile3.txt", "w") as f:
        f.write("The sun set beautifully.\n")
        f.write("The kids laughed joyfully.\n")
except Exception as e:
    print(e)
#? ---
    
with open("myFile.txt", "r") as f:
    for line in f:
        print(line)