# ---------------------------------------------------------------------------- #
#                                   argparse                                   #
# ---------------------------------------------------------------------------- #
from argparse import ArgumentParser

parser = ArgumentParser(description="   Welcome ".center(70, "*"))

# add_argument parameters
# required=True -> The argument must be given

parser.add_argument('name', help="Enter your name")
parser.add_argument('age', help="Enter your age", type=int)
parser.add_argument('-v', '--verbose', help="Print verbose", action='store_true')
args = parser.parse_args()
print(args.name)
print(args.age)

if args.verbose:
    print(f'Entered Name is: {args.name} and age: {args.age}')
