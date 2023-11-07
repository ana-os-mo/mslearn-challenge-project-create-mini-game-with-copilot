import random

# Function to get the user's choice
def get_user_choice():
    user_choice = input("\nEnter your choice: ").lower()
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        return user_choice
    else:
        print("Invalid choice. The valid options are 'rock', 'paper', or 'scissors'. Please try again.\n")
        return get_user_choice()

# Function to get the computer's choice
def get_computer_choice():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        return "rock"
    elif computer_choice == 2:
        return "paper"
    else:
        return "scissors"

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    user_wins = "You win!"
    computer_wins = "You lose!"

    if user_choice == computer_choice:
        print("It's a tie!")
        return 0
    elif user_choice == "rock":
        if computer_choice == "paper":
            print(computer_wins)
            return -1
        else:
            print(user_wins)
            return 1
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print(computer_wins)
            return -1
        else:
            print(user_wins)
            return 1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print(computer_wins)
            return -1
        else:
            print(user_wins)
            return 1
