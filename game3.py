import game_functions

# this version is the same as game2.py but has a score and the functions are in another file

player = True

player_score = 0
comp_score = 0

# used a while loop to keep it running while the condition is True, listing all the possible outcomes.
while player:
    # sets the score for both to 0

    # this calls the player_choice function
    player = game_functions.player_choice()
    # this calls the comp_choice function
    computer = game_functions.comp_choice()

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

    if game_functions.game_tie(player, computer):
        player_score += 1
        comp_score += 1
        print(f"It's a tie! Computer: {comp_score}, You: {player_score}")

    elif game_functions.determine_winner(player, computer):
        player_score += 1
        print(f"You win! Computer: {comp_score}, You: {player_score}")
    else:
        comp_score += 1
        print(f"You lose! Computer: {comp_score}, You: {player_score}")
    play_again = input('Play again? (y/n): ').lower()
    if play_again != 'y':
        break



