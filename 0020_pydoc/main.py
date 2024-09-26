'''
 # @ Author: Sazin Reshed Samin
 # @ Create Time: 2024-09-10 17:06:22
 # @ Modified by: Sazin Reshed Samin
 # @ Modified time: 2024-09-11 09:28:44
 # @ Description:
 '''
import pydoc
import os


def skip_divider_by_zero(func):
    '''
    Params: function to be called
    Return: function which passed as argument
    '''

    def inner_divide(a, b):
        if b == 0:
            print("Can't divide by 0")
            return 
        return func(a, b)
    return inner_divide

@skip_divider_by_zero
def divider(a, b):
    return a / b

print(divider(1, 2))
print(divider(1, 0))

#os.chdir('0020_pydoc')

#pydoc.writedoc('main')