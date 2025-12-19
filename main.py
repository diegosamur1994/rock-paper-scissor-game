# Rock paper scissors game
import random

emojis = { 'r': '🪨', 'p': '📄', 's': '✂️'}
choices = ('r', 'p', 's')

# Asks user choice input r/p/s
while True:
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice")
        continue
# Computer chooses randomly r/p/s
    computer_chose = random.choice(choices)
    
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_chose]}")

    if user_choice == computer_chose:
        print("It's a tie")

    elif (
        (user_choice == "r") and (computer_chose == "p") or 
        (user_choice == "p") and (computer_chose == "s") or 
        (user_choice == "s") and (computer_chose == "r")):
        print("You lose")
    else:
        print("You win!")

    should_continue = input("Continue playing? (y/n): ").lower()
    if should_continue == "n": 
        break


        