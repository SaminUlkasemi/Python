# ---------------------------------------------------------------------------- #
#                                   sys.argv                                   #
# ---------------------------------------------------------------------------- #
import sys

print("Total argument: ", len(sys.argv))
print("Name of the Python script: ", sys.argv[0]) # sys.argv[0] is the name of the current Python script. 
print("Arguments passed: ")
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
