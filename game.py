import random  # imported the random module to use the randint method

# assigning rock, paper, scissors to game variable in a list
game = ['Rock', 'Paper', 'Scissors']

# assigning a single item of the list and converting it into a string
computer = str(game[random.randint(0, 2)])

# Boolean value, not assigning True to a variable
player = True

# used a while loop to keep it running while the condition is True, listing all the possible outcomes.
while player == True:
    # prompts the user to input either R, P or S
    player = input("Rock, Paper, Scissors? Input R, P or S ")
    if player == 'R':
        print('You played Rock')
        # this prints the user input as Rock, as opposed to R
    if player == 'S':
        print('You played Scissors')
    if player == 'P':
        print('You played Paper')
    print(f'Computer plays {computer}')
    # this prints the computer input as the word
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose!", computer, "wraps", 'Rock')
        else:
            print("You win!", 'Rock', "smashes", computer)
    elif player == "P":
        if computer == "S":
            print("You lose!", computer, "cut", 'Paper')
        else:
            print("You win!", 'Paper', "wraps", computer)
    elif player == "S":
        if computer == "R":
            print("You lose...", computer, "smashes", 'Scissors')
        else:
            print("You win!", 'Scissors', "cut", computer)
    else:  # this prints if the input is not R, P or S
        print("That's not a valid input. Please enter again")


# this is to play again but not complete yet
#     play_again = input('Play again? (y/n): ')
#     if play_again != 'y':
#         player == False
#     else:
#         break

# could we have converted the user input?