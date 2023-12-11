import random

def play_hangman():
    word_list = ["python", "java", "kotlin", "javascript", "ruby"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letter_guessed = set()
    tries = 6
    print("The word contains", len(word), "letters.")
    while len(word_letters) > 0 and tries > 0:
        print("You have", tries, "tries left.")
        if len(letter_guessed) == 0:
            print("Available letters:", "".join(alphabet))
        else:
            print("Available letters:", "".join(alphabet - letter_guessed))
        guess = input("Please guess a letter: ").lower()
        if guess in alphabet - letter_guessed:
            letter_guessed.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Good job! The word now is:", end=" ")
                for letter in word:
                    if letter in letter_guessed:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                print()
            else:
                tries -= 1
                print("Oops! That letter is not in the word:", end=" ")
                for letter in word:
                    if letter in letter_guessed:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                print()
        else:
            print("You've already guessed that letter. Try again:", end=" ")
            for letter in word:
                if letter in letter_guessed:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print()
    if tries == 0:
        print("You lost! The word was", word + ".")
    else:
        print("Congratulations! You won! The word was", word + ".")

if __name__ == '__main__':
    print("Welcome to the game of Hangman!")
    play_hangman()
