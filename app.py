from game_flow import play_game, play_again

# Function to start the game
def start_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will play against the computer.")
    print("Rock beats scissors. Scissors beats paper. Paper beats rock.")
    print("Please enter your choice. The valid options are 'rock', 'paper', or 'scissors'.")
    while True:
        play_game()
        if not play_again():
            break

# Start the game
start_game()
