# ---------------------------------------------------------------------------- #
#                                 Randomization                                #
# ---------------------------------------------------------------------------- #
# Ref: https://www.tutorialsteacher.com/python/random-module
# Ref: https://www.programiz.com/python-programming/modules/random

import random

# random.random() method returns a random float number between 0.0 to 1.0
print(random.random())

# random.randint() method returns a random integer between the specified integers
print(random.randint(1, 50))

# random.randrange() method returns a randomly selected element from the range created 
# by the start, stop and step arguments
print(random.randrange(50, 100, 10))

print("random.choice(\"LinuxOS\"): ", random.choice("LinuxOS"))
print("random.choice([12, 34, 45, 4546, 51]): ", random.choice([12, 34, 45, 4546, 51]))

numList = [234, 56, 34,786, 76, 67]
random.shuffle(numList)
print("numList shuffle: ", numList)
random.shuffle(numList)
print("numList shuffle: ", numList)