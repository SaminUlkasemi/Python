# ---------------------------------------------------------------------------- #
#                                   argparse                                   #
# ---------------------------------------------------------------------------- #
# Ref: https://www.youtube.com/watch?v=aGy7U5ItLRk

from argparse import ArgumentParser
import os

# TODO 4 steps to work with argparse
# TODO 1st: Get instance of ArgumentParse()
# TODO 2nd: add_argument using add_argument() method
# TODO 3rd: Parse the argument 
# TODO 4th: use the argument by name

# ---------------------------------------------------------------------------- #
#                   TODO 1st: Get instance of ArgumentParse()                  #
# ---------------------------------------------------------------------------- #
parser = ArgumentParser(description="   Welcome ".center(70, "*"))

#* Two types of argument argparse take
#* Positional arguments & options

# add_argument parameters
# required=True -> The argument must be given
# action='source_true' -> this action parameter will provide information about the argument 
# has put in the command line or not, like(if the argument is "-verbose") then if user put -v in cli
# then args.v value become true otherwise it value become false

# ---------------------------------------------------------------------------- #
#              TODO 2nd: add_argument using add_argument() method              #
# ---------------------------------------------------------------------------- #
# --------------------------- Positional arguments --------------------------- #
parser.add_argument('name', help="Enter your name")
# With type restriction
parser.add_argument('age', help="Enter your age", type=int)

# ---------------------------------- Options --------------------------------- #
parser.add_argument('-n', 
                    '--number', 
                    help="Provide a number", 
                    type=int,                   # type resitriction
                    choices=[1, 2, 3],          # choice restriction
                    default=0                   # default value
                    )

parser.add_argument(
                    '-v', 
                    '--verbose', 
                    help="Print verbose", 
                    action='store_true', 
                    )

parser.add_argument(
                    '-p',
                    '--print',
                    help='Print a message, use -pp for more verbose message',
                    action='count'                 
)

# ---------------------------------------------------------------------------- #
#                         TODO 3rd: Parse the argument                         #
# ---------------------------------------------------------------------------- #
args = parser.parse_args()

# ---------------------------------------------------------------------------- #
#                      TODO 4th: use the argument by name                      #
# ---------------------------------------------------------------------------- #
print(args.name)
print(args.age)

if args.verbose:
    print(f'Entered Name is: {args.name} and age: {args.age}')

if args.number == 0:
    print("Default option")
elif args.number == 1:
    print("Option1")
elif args.number == 2:
    print("Option2")
elif args.number == 3:
    print("Option3")


if args.print == 1:
    print(os.name)
elif args.print == 2:
    print(f'This os is {os.name}')
else:
    print("Default OS")
