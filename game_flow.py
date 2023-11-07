from game_logic import get_user_choice, get_computer_choice, determine_winner

# Initialize scores
player_score = 0
computer_score = 0
ties = 0
rounds_played = 0

# Function to play the game
def play_game():
    global player_score, computer_score, rounds_played, ties

    rounds_played += 1
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose " + user_choice + ".")
    print("The computer chose " + computer_choice + ".")
    result = determine_winner(user_choice, computer_choice)
    if result == 1:
        player_score += 1
    elif result == -1:
        computer_score += 1
    else:
        ties += 1
    print(f"Player Score: {player_score}, Computer Score: {computer_score}, Ties: {ties}\n")

# Function to play again
def play_again():
    global player_score, computer_score, rounds_played, ties
    while True:
        user_input = input("Would you like to play again? (y/n) ").lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            print(f"\nFinal Scores - Player: {player_score}, Computer: {computer_score}")
            print(f"Rounds Played: {rounds_played}, Ties: {ties}")
            if player_score > computer_score:
                print("You won!")
            elif player_score < computer_score:
                print("The computer won!")
            else:
                print("It's a tie!")
            print("Thanks for playing!")
            return False
        else:
            print("Invalid choice. The valid options are 'y' to play again or 'n' to quit the game. Please try again.\n")