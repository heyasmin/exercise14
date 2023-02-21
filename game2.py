import random  # imported the random module to use the randint method

# issues to fix: computer keeps picking scissors rather than random, and player doesn't lose

# assigning rock, paper, scissors to game variable in a list
game = ['R', 'P', 'S']
computer = str(game[random.randint(0, 2)])


# Boolean value, it's not assigning True to a variable
player = True


# Keeps asking the player for input until they enter "R", "P", or "S" only. Invalid if they don't.
def player_choice():
    _player = input("Rock, Paper, Scissors? Input R, P or S: ")
    while _player != 'R' and _player != 'P' and _player != 'S':
        print(f"That's not a valid input. Please input again.")
        _player = input("Rock, Paper, Scissors? Input R, P or S: ")
    return _player


# Randomly selects either "rock", "paper" or "scissors" for computer to return from game list
def comp_choice():
    _computer = game[random.randint(0, 2)]
    if _computer == 0:
        return 'R'
    elif _computer == 1:
        return 'P'
    else:
        return 'S'


# This returns true if there is a tie
def game_tie(_player, _computer):
    return _player == _computer


# This returns true if the player wins
def player_win(_player, _computer):
    winner = (_player == "R" and _computer == "S") or (_player == "P" and _computer == "R") or (
            _player == "S" and _computer == "P")
    return player_win


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

    elif player_win(player, computer):
        print('You win!')
    else:
        print('You lose!')
    play_again = input('Play again? (y/n): ')
    if play_again != 'y':
        break



