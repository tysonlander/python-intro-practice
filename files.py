# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open("myfile.txt", "w")

# Get some info
print("Name: ", myFile.name)
print("Is Closed: ", myFile.closed)
print("Opening mode: ", myFile.mode)

# Write to file
myFile.write("I love Python")
myFile.write(" and Javascript")
myFile.close()

# Append to file
myFile = open("myfile.txt", "a")
myFile.write(" I also like SCSS")
myFile.close()

# Read form file
myFile = open("myfile.txt", "r+")
text = myFile.read(10)
print(text)
