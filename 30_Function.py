# function = A block of reusable code
#            place () after the function name to invoke it 
# return = statement used to end a function and
#          send a result back to the caller.
#_____________________________________________________


# def happy_birthday(name,age):
#     print(f"Happy Birthday to {name}")
#     print(f"You are {age} years old! ")
#     print("Happy Bithday to You.")
#     print()

# happy_birthday("Ashraf",25)
# happy_birthday("ath",21)
# happy_birthday("jilan",14)

# def display_invoice(username, amount, due_date):
#     print(f"Hello, {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Shahin",42.50,"01/01")

# def add(x,y):
#     z = x+y
#     return z
# def subtract(x,y):
#     z = x-y
#     return z
# def Multiply(x,y):
#     z = x*y
#     return z
# def divide(x,y):
#     z = x/y
#     return z

# print(add(1,2))
# print(subtract(1,2))
# print(Multiply(1,2))
# print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last  = last.capitalize()
    return first + " " + last

full_name = create_name("ashraful", "azam" )
print(full_name)