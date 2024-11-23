# Membership operators: used to test whether a value or variable is found in a sequence
#           (such as a list, set, tuple, string, or dictionary).
#           1. in : returns True if the value is found in the sequence, False otherwise
#           2. not in : returns True if the value is not found in the sequence, False otherwise

food = ['pizza', 'sushi', 'tacos']
print('pizza' in food)  # Output: True
print('sushi' not in food)  # Output: False

fruit = "Apple"
print("a" in fruit)  # Output: True
print("b" not in fruit)  # Output: True

email = "john.doe@example.com"
if "@" in email and "." in email:
    print ("Valid email")  # Output: Valid email
else :
    print("Invalid email") 

dict = {"name": "John", "age": 30, "city": "New York"}

print("name" in dict)  # Output: True
print("age" not in dict)  # Output: False