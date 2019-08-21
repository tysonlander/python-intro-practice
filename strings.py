# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "tyson"
age = 30

# concat
print("hello " + name + " and i am " + str(age))

# String Formatting


# arguments by position
print("{1}, {2}, {0}".format("a", "b", "c"))

# arguments by name
print("My name is {name} and I am {age}".format(name=name, age=age))

# F-Strings (only in 3.6+)
print(f"My name is {name} and I am {age}")

# String Methods

s = "HellO there world"

# capitalize first lsetter
print(s.capitalize())

# make all uppercase
print(s.upper())

# make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace("world", "everyone"))

# Count
sub = "H"
print(s.count(sub))

# starts with
print(s)
print(s.startswith("HellO"))

# Ends with
print(s.endswith("d"))

# Split into a list
print(s.split())

# Find position
print(s.find("r"))

# Is all alphanumeric
print(s.isalnum())

