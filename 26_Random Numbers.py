import random

# print(help(random))
# Creating a random integer
# print(random.randint(1,6)) # print a random int number between  1 to 6
# low = 1
# high = 100
# number = random.randint(low,high)
#number = random.random() # prints a random float number form 0 to 1

# options = ("rock", "paper", "scissors")
# option= random.choice(options)
# print(option)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A",]
random.shuffle(cards)
print(cards)