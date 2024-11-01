# *args    = allows you to pass multiple non-key argumnets (type = Tuples)
# **kwargs = allows you to pass multiple keyword-arguments (Type = dictionary)
#          * unpaking operator 
#          1.positional 2. default 3. keyword 4.arbitary

# *Args:

# def add (a,b):
#     return a+b
# print(add(1,2))

#Instead of this , we can do this -> Using *args

# def add(*args): # here instead of args we can write any random texts
#     total = 0
#     for arg in args:
#         total+=arg
#     return total

# print(add(1,2,4,5,100)) #here we can add as much as value we want 

# def display_name(*args):
#     for arg in args:
#         print(arg , end=" ")

# display_name("Dr." , "Spongebob", "harold","Squarepants","III")

# # kwargs :
# def print_adress(**kwargs):
#     for key in kwargs.keys():
#         print(key, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value,end=" " )
#     print()
#     for key,value in kwargs.items():
#         print(key,":",value)

# print_adress(street="123 Fake St.",
#              city="Detorit",
#              state="Oasis",
#              zip="54321")

# Exercise:

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} , {kwargs.get('zip')}")

shipping_label("Dr." , "Spongebob", "harold","Squarepants","III",
                street="123 Fake St.",
                apt = "#100",
                city="Detorit",
                state="Oasis",
                zip="54321")