
# import random to generate random dice rolls
import random

# import time to add player suspense and improve game play flow
# Delay inspiration/reference: https://opensource.com/article/17/10/python-101
import time

def main():
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
    
    play_again = True

    while play_again:

        # Set game scores to zero
        player_game_total = 0
        opponent_game_total = 0
        
        # Randomly choose which player will roll first
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
                
                opponent_game_total = opponent_game_total + opponent_total_roll
            
            # Switch turns
            player_turn = not player_turn
            opponent_turn = not opponent_turn

            print("Score Board:")
            print("Your Score: " + str(player_game_total))
            print("Opponent's Score: " + str(opponent_game_total))
            print()
            time.sleep(2)
            
        if (player_game_total >= 100):
            print("You win! You are the first player to reach 100 points!\n")
        elif opponent_game_total >= 100:
            print("Your opponent reached 100 points before you did. You lose.\n")
        else:
            print("It's a tie! How is that even possible?!\n")
            
        again = input("Would you like to play again? Y/N: ")
        
        if (again != "Y" or "y"):
            play_again = False
        else:
             play_again = True

main()
