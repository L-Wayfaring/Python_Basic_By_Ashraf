# Iterables = An object / collection that can return  its elements one at a time,
#             allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print (number)
# for number in reversed(numbers):
#     print (number)

# same for sets(not reversible) and tuples.

# name = "L Wayfaring"
# for character in name:
#     print(character, end=" ")

# dictionary:

my_dictionary = {"A" : 1, "B" : 2, "C" : 3}

# for key in my_dictionary:
#     print (key) # only keys
for key in my_dictionary.keys():
    print(key) #print keys
print()
for value in my_dictionary.values():
    print(value)
for key, value in my_dictionary.items():
    print(f"{key} = {value}")