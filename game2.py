import random  # imported the random module to use the randint method

# issues to fix: convert the values with a dictionary!!!
# so it will print the player and computer choices in 2 lines of code

# assigning rock, paper, scissors to game variable in a list
game = ['R', 'P', 'S']
computer = str(game[random.randint(0, 2)])


# Boolean value, it's not assigning True to a variable
player = True


# Keeps asking the player for input until they enter "R", "P", or "S" only. Invalid if they don't.
def player_choice():
    player = input("Rock, Paper, Scissors? Input R, P or S: ")
    while player != 'R' and player != 'P' and player != 'S':  # this should be or, but it doesn't work, so I put and
        print(f"That's not a valid input. Please input again.")
        player = input("Rock, Paper, Scissors? Input R, P or S: ")
    return player


# Randomly selects either "rock", "paper" or "scissors" for computer to return from game list
def comp_choice():
    computer = game[random.randint(0, 2)]
    # if computer == 0:
    #     return 'R'
    # elif computer == 1:
    #     return 'P'
    # else:
    #     return 'S'
    return computer


# This returns true if there is a tie
def game_tie(player, computer):
    return player == computer


# This returns true if the player wins
def determine_winner(player, computer):
    winner = (player == "R" and computer == "S") or (player == "P" and computer == "R") or (
            player == "S" and computer == "P")
    return winner


# used a while loop to keep it running while the condition is True, listing all the possible outcomes.
while player:

    # this calls the player_choice function
    player = player_choice()
    # this calls the comp_choice function
    computer = comp_choice()

    # prints the choices
    if player == 'R':
        print('You played Rock.')
    if player == 'P':
        print('You played Paper.')
    if player == 'S':
        print('You played Scissors.')

    if computer == 'R':
        print('Computer played Rock.')
    if computer == 'P':
        print('Computer played Paper.')
    if computer == 'S':
        print('Computer played Scissors.')

    # this calls the tie function and checks it with an if statement
    if game_tie(player, computer):
        print("It's a tie!")

    elif determine_winner(player, computer):
        print('You win!')
    else:
        print('You lose!')
    play_again = input('Play again? (y/n): ')
    if play_again != 'y':
        break



