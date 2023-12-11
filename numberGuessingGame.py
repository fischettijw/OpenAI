import random
import tkinter as tk

# Generate a random number to guess
number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Add a label to display the instructions
label = tk.Label(root, text="Guess a number between 1 and 100:")
label.pack()

# Add an entry widget for the player's guess
entry = tk.Entry(root)
entry.pack()

# Add a button to submit the player's guess
button = tk.Button(root, text="Guess", command=lambda: guess_number())
button.pack()

# Add a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

def guess_number():
    global attempts
    attempts += 1

    # Get the player's guess
    guess = int(entry.get())

    # Check if the guess is correct
    if guess == number:
        result.set(f"Congratulations, you guessed the number in {attempts} attempts!")
        button.config(state="disabled")
    elif guess < number:
        result.set("The number is higher.")
    else:
        result.set("The number is lower.")

# Start the main loop
root.mainloop()
