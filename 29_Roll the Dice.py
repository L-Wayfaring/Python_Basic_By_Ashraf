import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌  ─ ┐ │ └ ┘

# "┌─────────┐"
 #"│         │"
 #"│         │"
 #"│         │"
 #"└─────────┘"
# Creating a dictionary which, keys= numbers: values: Tuples
dice_art = {
    1:( "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2:( "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3:( "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4:( "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5:( "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6:( "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
# Create a list
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# # displaying the dice Art: (Vertical)
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line ,end=" ")

# displaying the dice art : (Horizontal)
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end = "")
    print()
# Calculate the total:
for die in dice:
    total += die
print(f"Total: {total}")

## From : BRO CODE ## Thanks🥰