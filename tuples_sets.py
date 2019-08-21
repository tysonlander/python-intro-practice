# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#  simple tuple
# fruit_tuple = ("Apple", "Orange", "Mango")
#  Using constructor
# fruit_tuple = tupple(("Apple", "Orange", "Mango"))

# print(fruit_tuple[1])

# # Can not change value
# # fruit_tuple[1] = "Grape"

# fruit_tuple_2 = ("Apple",)
# del fruit_tuple_2
# print(fruit_tuple_2)


# print(fruit_tuple)


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {"Apple", "Orange", "Mango"}

# Check if in set
print("Apple" in fruit_set)

# Add to set
fruit_set.add("Grape")

# Remove from set
fruit_set.remove("Grape")

del fruit_set

print(fruit_set)

