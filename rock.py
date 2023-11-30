#TASK 4

import random

# Initialize scores
user_score = 0
computer_score = 0

while True:
# Prompt user to choose
    user_choice = input("Choose rock, paper, or scissors: ")

 # Generate computer's choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

# Display choices
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")

 # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

 # Display scores
    print(f"Your score: {user_score}, Computer's score: {computer_score}")

# Ask to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing!")
        break