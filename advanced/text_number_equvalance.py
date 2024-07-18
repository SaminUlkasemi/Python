# * Although the string value of a number is considered a completely different value from 
# * the integer or floating-point version, an integer can be equal to a floating point.
print(42 == '42')

print(42 == 42.0)

print(42.0 == 0042.000)

# Python makes this distinction because strings are text, while integers and floats are both numbers.