# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. No Duplicates

capitals = {"USA":"Washington D.C.",
            "Bangladesh":"Dhaka",
            "China":"Beijing",
            "Russia":"Moscow"}
# All of the different attributes and methods of dictionaries: 
# print(dir(capitals))
# In depth description methods:
# print(help(capitals))

# print(capitals.get("Bangladesh"))

# if capitals.get("Bangladesh"):
#     print("The capital exists!")
# else:
#     print("This capital doesn't exist!")

#Update a dictionary
#capitals.update({"Germany":"Berlin"})

#Remove from dictionary
#capitals.pop("China")

#Remove the latest element from a dictionary 
# capitals.popitem()

# Clearing the dictionary
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key, end=" ") # USA Bangladesh China Russia 
# print()
# values = capitals.values()
# for value in capitals.values():
#      print(value, end=" ") # Washington D.C. Dhaka Beijing Moscow
# items = capitals.items()
# print(items)
for key,value in capitals.items():
    print(f"{key}:{value}")