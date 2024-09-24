# collection = single "variable" used to store multiple values
# List  = [] ordered and changable. Duplicates OK.
# Set   = {} unordered and immutable, but add/remove OK. No duplicates
# Tuple = () ordered and unchangeable . Duplicates Ok. Faster

#Collection:

# fruit = "banana"

#Lists:
# fruits = ["apple","orange","banana","coconut"]
#print(fruits) # print all fruits.

# print(fruits[0]) # Accessing fruits by indexing # output: apple

# print(fruits[::-1]) #Accessing them in reverse

# for fruit in fruits:          # Accessing them by for loops
#     print(fruit)

#print (dir(fruits)) #All the methods that are applicable for a list will be displaied
#print(len(fruits))     # Length of fruits

# print("apple" in fruits)  # is there any apple in fruits

#fruits [0] = "pineapple"

#fruits.append("pineapple")      #add an element to a list

#fruits.remove("apple")

#fruits.insert(0,"pineapple") #insert an element at a particular index
# fruits.sort() #sort Alphabetical order
# fruits.reverse() # reverse order
# fruits.clear() #Empty a list 
# print(fruits.index("apple")) # Find the index of a valid element
#print(fruits.count("banana"))


#Set:
fruits  = {"apple","orange","banana","coconut"}
#print(dir(fruits))
#print(help(fruits))
# print (len(fruits))
#print("pineapple" in fruits) # false
#print(fruits[0]) #TypeError: 'set' object is not subscriptable
# fruits.add("pineapple")
# fruits.remove("pineapple")
# fruits.pop() # pop an element randomly from set

#Tuple:
fruits  = ("apple","orange","banana","coconut","coconut")
#print(dir(fruits))
#print(help(fruits))
# print (len(fruits))
#print("pineapple" in fruits) # false

print(fruits.index("coconut")) # 3 (first priority)
print(fruits.count("coconut")) # 2

for fruit in fruits:
     print(fruit)