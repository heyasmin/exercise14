
import random


# imported random module which enables the computer to select a random value

# *make note
game_on = True

# * ^make note
user_score = 0
comp_score = 0
# *make note
number_of_rounds = 0
# * ^make note



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

weapons = {"R":"rock","P":"Paper","S":"scissors"}random

 # if user_decision == 'R':
 #        user_decision = 'rock'
 #    elif user_decision == 'S':
 #        user_decision = 'scissors'
 #    elif user_decision == 'P':
 #        user_decision = 'paper'
 #    else:
 #        print('try again, pick either R , P, or S.')
 #
 #    return user_decision, computer_decision

# *make note



number_of_rounds += 1



# * ^make note

# using an if conditional to assign the letter (that's inputted by the user) to acronym/object
# This allows the computer to convert the value into the assigned acronyms
# while making a logical comparison between the value and the user's input
# elif is short for "else if" and is used when the first if statement isn't true, but you want to check for another condition


# # *make note
# number_of_rounds += 1
# # * ^make note

def decide_who_wins(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
        # comp_score +=1 and user_score += 1
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
            print("Your score: ", user_score, ".. computer's score:", comp_score)
        else:
            print("Paper covers rock! You lose.")
            comp_score += 1
            print("Your score: ", user_score, ".. computer's score:", comp_score)
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
            print("Your score: ", user_score, ".. computer's score:", comp_score)
        else:
            print("Scissors cuts paper! You lose.")
            comp_score += 1
            print("Your score: ", user_score, ".. computer's score:", comp_score)
    elif user_choice == "scissors":
        if computer_choice == "paper":
            user_score += 1
            print("Scissors cuts paper! You win!")
            print("Your score: ", user_score, ".. computer's score:", comp_score,)
        else:
            print("Rock smashes scissors! You lose.")
            comp_score += 1
            print("Your score: ", user_score, ".. computer's score:", comp_score)


user, computer = choose_weapon()
decide_who_wins(user, computer)

# the game was created here using an if loop, with different messages to display the comparison
# between the computers choice and user's choice


# I use an IF statement because it enables be to create a logical comparison
# between a value and what is expected by testing for a condition
# and returning a result if that condition is True or False.

# *make note
print("---------------------")
print("")
print(f"Round Number",number_of_rounds,)
print("-----------Score Board------------")
print("Your score: ",user_score,".. computer's score:",comp_score)
print("===========")
print("")

# play_again = input('Play again? (y/n)')
# if play_again != 'y':
#     break

if number_of_rounds==5:
    game_on = False




# * ^make note
