
import random


# imported random module which enables the computer to select a random value

def choose_weapon():
    weapons = ['rock', 'paper', 'scissors']
    # print(play[0])
    # create list of play options

    computer_decision = weapons[random.randint(0, 2)]
    #  randint generates a function that selects an integer selected at random.
    # this integer is assigned to the index of the values in the play variable
    user_decision = input("Enter a value of (R , P, or S):  ").upper()

    # # # created a variable where we assigned an input which allows the user to
    # # # pick between objects rock, paper and scissors

    if user_decision == 'R':
        user_decision = 'rock'
    elif user_decision == 'S':
        user_decision = 'scissors'
    elif user_decision == 'P':
        user_decision = 'paper'
    else:
        print('try again, pick either R , P, or S.')

    return user_decision, computer_decision



# using an if conditional to assign the letter (that's inputted by the user) to acronym/object
# This allows the computer to convert the value into the assigned acronyms
# while making a logical comparison between the value and the user's input
# elif is short for "else if" and is used when the first if statement isn't true, but you want to check for another condition
#
# if comp_game == 0:
#     comp_action = 'rock'
# if comp_game == 1:
#     comp_action = 'paper'
# else:
#     comp_action = "scissors"


#  here, the if statement is assigning the index number to the list objects
#  whilst generating the computers actions , e.g. picking scissors at random

# print(f" Computer chose {computer_decision}. \n")


#  Printing the random object that the computer generated

# if user_decision == comp_action:
#     print("it's a tie!")
# elif user_decision == "rock":
#     if comp_action == "paper":
#         print("You lose!", comp_action, "covers", user_decision)
#     else:
#         print("You win!", user_decision, "smashes", comp_action)
# elif user_decision == "paper":
#     if comp_action == "scissor":
#         print("You lose!", comp_action,"snips through", user_decision)
#     else:
#         print("You win", user_decision, "covers", comp_action)
# elif user_decision == "scissor":
#     if comp_action == "rock":
#         print("you lose!", user_decision, "smashes", comp_action)
#     else:
#         print("u win!", user_decision, "cuts", comp_action)

def decide_who_wins(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


user, computer = choose_weapon()
decide_who_wins(user, computer)

# the game was created here using an if loop, with different messages to display the comparison
# between the computers choice and user's choice


# I use an IF statement because it enables be to create a logical comparison
# between a value and what is expected by testing for a condition
# and returning a result if that condition is True or False.
