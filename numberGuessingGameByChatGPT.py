import random

# Generate a random number to guess
number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Start the game loop
while True:
    # Get the player's guess
    guess = int(input("Guess a number between 1 and 1000: "))
    attempts += 1

    # Check if the guess is correct
    if guess == number:
        print(f"Congratulations, you guessed the number in {attempts} attempts!")
        break
    elif guess < number:
        print("The number is higher.")
    else:
        print("The number is lower.")
