import random  # imported the random module to use the randint method

# assigning rock, paper, scissors to game variable in a list
game = ['R', 'P', 'S']

# assigning a single item of the list and converting it into a string
# computer = game[random.randint(0, 2)]

# Boolean value, not assigning True to a variable
player = True

# used a while loop to keep it running while the condition is True, listing all the possible outcomes.
while player:
    # prompts the user to input either R, P or S
    computer = game[random.randint(0, 2)]
    player = input("Rock, Paper, Scissors? Input R, P or S: ")
    if player == 'R':
        print('You played Rock.')
        # this prints the user input as Rock, as opposed to R
    if player == 'S':
        print('You played Scissors.')
    if player == 'P':
        print('You played Paper.')
    if computer == 'R':
        print('Computer played Rock.')
        # this prints the user input as Rock, as opposed to R
    if computer == 'S':
        print('Computer played Scissors.')
    if computer == 'P':
        print('Computer played Paper.')
    # this prints the computer input as the word
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print(f'You lose! Paper wraps Rock.')
        else:
            print(f'You win! Rock smashes Scissors.')
    elif player == "P":
        if computer == "S":
            print(f'You lose! Scissors cut Paper.')
        else:
            print(f'You win! Paper wraps Rock.')
    elif player == "S":
        if computer == "R":
            print(f'You lose! Rock smashes Scissors.')
        else:
            print(f'You win! Scissors cut Paper.')
    else:  # this prints if the input is not R, P or S
        print(f"That's not a valid input. Please play again.")
    play_again = input('Play again? (y/n): ')
    if play_again != 'y':
        break

