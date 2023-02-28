# this version is the same as game3.py but need to have the game values in a dictionary
import game_functions

player = True

player_score = 0
comp_score = 0

# used a while loop to keep it running while the condition is True, listing all the possible outcomes.
while player:

    player = game_functions.player_choice()
    computer = game_functions.comp_choice()

    print(f'You played {player} \nComputer played {computer}')

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
