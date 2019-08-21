# A List is a collection which is ordered and changeable. Allows duplicate members.

# numbers = [1, 2, 3, 4, 5]
numbers = list((1, 2, 3, 4, 5))
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# get value
print(fruits[1])

# get len
print(len(fruits))

# Append to list
fruits.append("Mangos")
print(fruits)

# Remove form list
fruits.remove("Grapes")
print(fruits)

# Insert into position
fruits.insert(2, "Strawberries")
print(fruits)

# Remove form position
fruits.pop(2)


# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)

