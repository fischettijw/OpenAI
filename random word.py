# https://pypi.org/project/Random-Word/

import os; os.system("cls")

from random_word import RandomWords
r = RandomWords()

# Return a single random word
word = r.get_random_word()
# print(word)

while len(word) > 7:
    word = r.get_random_word()
    
print(word)
 
