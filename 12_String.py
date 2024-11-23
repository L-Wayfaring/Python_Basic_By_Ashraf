# name = input("Enter your full name: ")

name = "L. Wayfaring"

# To print the length of a string , len()
string_length = len(name)

# # To find a letter , name.find()
find_char = name.find("i") # print it's position at 9th(as indexing from 0)

# #To capitalaized the first Letter , name.capitalize ()
capitalize = name.capitalize() # L. wayfaring

# #To uppercase , name.upper()
Upper = name.upper() # L. WAYFARING

# # To lowercasse , name.lower()
lower = name.lower() # l. wayfaring

# # To check is the string is in digit
isdigit = name.isdigit() # False ? Only digit is accepted

# # To check string is in alphabet
isalphabet = name.isalpha() # False > Only alphabet is accepted

# # To count somethig on a string .(like how many 'a' are there in name)
name.count("a")
count = name.count("a") # 2

# # To replace one character to another , name.replace("" , "")
replace = name.replace("L","G")

# To find comprehensive list of all these string operation
print(help(str))

# Ex: 1
# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter Your name : ")

length = len(username)
spaces = username.find(" ")

if length > 12 :
    print("Enter Your name that is no more than 12 characters!")
elif not spaces == -1:
    print("Enter Your name without spaces! ")
elif not username.isalpha():
    print("Enter name without digits! ")
else:
    print(f"Hi,{username} !")