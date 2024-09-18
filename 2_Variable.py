# Variable = A container for a value (string , integer, float, boolean)
#            A variable behaves as if it was the value it contains

#S t r i n g s . . .

first_name = "Ashraf"
food = "pizza"
email = "bro123@fake.com"

print(first_name)

""" To display my name with some texts We have to use F-string. (F -> Format)
 To use Formatted string literals , begin a string with f or F before the opening quotation mark or tripple quotation mark.
 Inside this string , you can write a Python expression between { and } characters that can refer to variables or literal values. """

print(f"Hello, {first_name}.")
print(f"You like {food}.")
print(f"Your email is {email}")

# I n t e g e r . . .

age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

# F l o a t . . .

price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is : {gpa}")
print(f"You ran {distance} km.")

# B oo l e a n . . .

is_student = False

if is_student:
    print("You are a student.")
else:
    print("Your are not a Student.")

for_sale = True

if for_sale:
    print("That item is for sale.")
else:
    print("That item is not for sale.")

#Complex Number

complex_num = (2+ 3j) 

