
# import random to generate random dice rolls
import random

# import time to add player suspense and improve game play flow
# Delay inspiration/reference: https://opensource.com/article/17/10/python-101
import time

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

player_game_total = 0
opponent_game_total = 0

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

# Display results of opponent's turn.
# Add time delays for player suspense and game play flow

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

opponent_game_total = opponent_game_total + opponent_total_roll






