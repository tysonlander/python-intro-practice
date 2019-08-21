# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["John", "Will", "Janet", "sam"]

# Simple for Loop


# Break out
# for person in people:
#     if person == "Janet":
#         break
#     print("Current person: ", person)

# Continue
# for person in people:
#     if person == "Janet":
#         continue
#     print("Current person: ", person)

# Range
# for i in range(len(people)):
#     print("Current Person: ", people[i])

# for i in range(0, 4):
#     print("hello ", people[i])


# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 30:
    print("Count: ", count)
    count += 1