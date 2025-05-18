import random

# Create a head or tails game using random.randint

heads = 0
tails = 1

# Welcome message
# ------------------------------------------------------------
print("Welcome to the Heads or Tails game!")
print("Please enter your guess:")

# Input from a user to determine their guess 0 for the heads or 1 for tails
# ------------------------------------------------------------
flip_input = int(input("Enter 0 for heads or 1 for tails:\n "))

# Create variable to set random number for coin flip
coin_flip = random.randint(0, 1)

# Condition to determine if the coin flip is heads or tails
# ------------------------------------------------------------
if coin_flip == 0:
    print("Heads")
else:
    print("Tails")

# Condition to determine if the user wins or loses
# ------------------------------------------------------------
if flip_input == coin_flip:
    print("You win!")
else:
    print("You lose!")