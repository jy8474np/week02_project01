
# import random to generate random dice rolls
import random

# import time to add player suspense and improve game play flow
# Time delay inspiration/Ref: https://opensource.com/article/17/10/python-101
import time

# Define the main function that will contain and run all
def main():
    # Display introduction, game rules, and teaser
    print("Welcome to Race Ya!")
    time.sleep(2)
    print("The objective is simple: Be the first player to reach 100 points.")
    print("Can you reach 100 points before your opponent does?")
    time.sleep(3)
    print("Ready ...")
    time.sleep(1)
    print("Set ...")
    time.sleep(1)
    print("Race Ya!")
    time.sleep(2)
    print()
    
    # Define play_again for continual play start/stop
    play_again = "y"

    # Begin game play loop Ref: https://dev.to/oxy_oxide/dice-rolling-game-using-python-pn
    while play_again == "y" or play_again == "Y":

        # Set game scores to zero
        player_game_total = 0
        opponent_game_total = 0
        
        # Randomly choose which player will roll first Ref: https://codereview.stackexchange.com/questions/94116/turn-based-battle-simulator
        turn = random.randint(1,2)
        if turn == 1:
            player_turn = True
            opponent_turn = False
            print("You get to roll first!\n")
            time.sleep(1)
        else:
            player_turn = False
            opponent_turn = True
            print("Your opponent will roll first.\n")
            time.sleep(1)
        
        # Start game_total tracking loop
        while (player_game_total < 100 and opponent_game_total < 100):
            
            # create two dice for the player, with each die comprised of values from one to six
            player_die01 = random.randint(1,6)
            player_die02 = random.randint(1,6)
            
            # Calculate the sum of die01 and die02 to determine the player's roll total
            player_total_roll = player_die01 + player_die02
            
            # create two dice for the opponent, with each die comprised of values from one to six
            opponent_die01 = random.randint(1,6)
            opponent_die02 = random.randint(1,6)
            
            # Calculate the sum of die01 and die02 to determine the opponents's roll total
            opponent_total_roll = opponent_die01 + opponent_die02

            if player_turn:
                # Display results of player's turn.
                # Add time delays for player suspense and game play flow
                print("You rolled:")
                time.sleep(1)
                print(player_die01)
                time.sleep(1)
                print ("... and ...")
                time.sleep(1)
                print(player_die02)
                time.sleep(1)
                print("... for a total of ...")
                time.sleep(1)
                print(str(player_total_roll))
                print()
                time.sleep(2)
                
                # Create a counter to calulate player's running total
                player_game_total = player_game_total + player_total_roll

            else:
                # Display results of opponent's turn.
                # # Add time delays for player suspense and game play flow
                print("Your opponent rolled:")
                time.sleep(1)
                print(opponent_die01)
                time.sleep(1)
                print ("... and ...")
                time.sleep(1)
                print(opponent_die02)
                time.sleep(1)
                print("... for a total of ...")
                time.sleep(1)
                print(str(opponent_total_roll))
                print()
                time.sleep(2)
                
                # Create a counter to calculate opponent's running total
                opponent_game_total = opponent_game_total + opponent_total_roll
            
            # Switch turns Ref: https://codereview.stackexchange.com/questions/94116/turn-based-battle-simulator
            player_turn = not player_turn
            opponent_turn = not opponent_turn

            # Display an up-do-date score board after each turn
            print("Score Board:")
            print("Your Score: " + str(player_game_total))
            print("Opponent's Score: " + str(opponent_game_total))
            print()
            time.sleep(2)
        
        # Display game result message and final scores
        if (player_game_total >= 100):
            print("You win! You are the first player to reach 100 points!\n")
            print("Final Scores:")
            print("Your Score: " + str(player_game_total))
            print("Opponent's Score: " + str(opponent_game_total))
            print()
            time.sleep(2)
        elif opponent_game_total >= 100:
            print("Your opponent reached 100 points before you did. You lose.\n")
            print("Final Scores:")
            print("Opponent's Score: " + str(opponent_game_total))
            print("Your Score: " + str(player_game_total))
            print()
            time.sleep(2)
        else:
            print("It's a tie! Where are we, Europe?!\n")
            print("Final Scores:")
            print("Your Score: " + str(player_game_total))
            print("Opponent's Score: " + str(opponent_game_total))
            print()
            time.sleep(2)
        
        # Prompt user if they want to play again
        play_again = input("Would you like to play Race Ya! again? Y/N: ")

main()
