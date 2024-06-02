import math

first = "Dave"
last = "Gray"

# print(type(first)) # Prints data type
# print(type(first) == str) # Prints out TRUE/FALSE
# print(isinstance(first, str)) # Prints out TRUE/FALSE

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting number to string
decade = str(1980)
print(type(decade))

statement = "I like music from the " + decade + "s."
print(statement)

# Multi lines
multiline = '''
Hey, how are you?

I was just checking in.
                            All good?

'''
print(multiline)

# Escaping special characters
# \n indicates new line
# \' allows a ' to be used
# \\ shows as a single backslash
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower()) # all lowercase
print(first.upper()) # ALL UPPERCASE

print(multiline.title()) # capitalises all words
print(multiline.replace("good", "ok")) #  replaces good with ok
print(multiline) # original version

print(len(multiline)) # length of var
multiline += "                          "
multiline = "                               " + multiline
print(len(multiline))

print(multiline.strip()) # removes whitespace

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

# String Index Values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[0:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x)) # Type of variable
print(isinstance(myvalue, bool))

# Numeric data types

# Integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float
gpa = 3.28
y  = float(1.14)
print(type(gpa))

# Complex
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers
print(abs(gpa)) # checks absolute value
print(round(gpa)) # rounds to nearest integer
print(round(gpa, 1)) # rounds to nearest DP

print(math.pi)
print(math.sqrt(144))
print(math.ceil(gpa)) # rounds UP to nearest integer
print(math.floor(gpa)) # rounds DOWN to nearest integer

# Casting a string to number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))