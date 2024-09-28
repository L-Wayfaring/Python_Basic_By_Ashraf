# Concession stand program
# dictionary {key:value}

menu ={
    "pizza":3.00,
    "nachos":4.50,
    "popcorn":6.00,
    "chips":1.00,
    "pretzel":3.50,
    "soda":3.00,
    "lemonade":4.25
    }
cart = [] # an empty list for adding items
total = 0
print("-----------Menu-----------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("__________________________________")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food) 

print("_______________Your Order___________________")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is : ${total:.2f}")

# From Bro Code