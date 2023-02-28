# game functions
import random

game = ('R', 'P', 'S')
# game_dict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
# mydict = {'letters': ['R', 'P', 'S'],
#           'words': ['Rock', 'Paper', 'Scissors']}


def player_choice():
    player = input("Rock, Paper, Scissors? Input R, P or S: ").upper()
    while player not in game:
        print(f"That's not a valid input. Please input again.")
        player = input("Rock, Paper, Scissors? Input R, P or S: ").upper()
    return player


# Randomly selects either "rock", "paper" or "scissors" for computer to return from game list
def comp_choice():
    computer = game[random.randint(0, 2)]
    return computer


# This returns true if there is a tie
def game_tie(player, computer):
    return player == computer


# This returns true if the player wins
def determine_winner(player, computer):
    winner = (player == "R" and computer == "S") or (player == "P" and computer == "R") or (
            player == "S" and computer == "P")
    return winner
