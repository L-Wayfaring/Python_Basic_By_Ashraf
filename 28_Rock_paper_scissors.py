import random

options= ("ROCK","PAPER","SCISSOR")
Playing = True

while Playing:

    player = None
    computer = random.choice(options)
    while player not in options:            # While user don't push input from "Options" the while loop continuous forever! Mua ha ha ha😈😈😈

        player = input("Enter a choice (rock 👊, paper 🖐️, scissor ✌️ ): ").upper()

    print(f"Player 😎: {player}")
    print(f"Computer🤖: {computer}")

    if player == computer:
        print("Dang! It's a tie! 😎👊🤖")

    elif player == "ROCK" and computer == "SCISSOR":
        print("Yo Bruh! You Win!😍😍😍")

    elif player == "PAPER" and computer == "ROCK":
        print("Yo Bruh! You Win!😍😍😍")

    elif player == "SCISSOR" and computer == "PAPER":
        print("Yo Bruh! You Win!😍😍😍")

    else:
        print("Have a relax! See you! Not for mind!😂😂😂")
    
    # play_again = input("Play again?😊(y/n): ").lower()
    # if not play_again == "y":
    #     Playing = False
    if not input("Play again?😊(y/n): ").lower() == "y":
        Playing = False

print("Thanks For Playing 🥰🥰🤗🤗🥰🥰")