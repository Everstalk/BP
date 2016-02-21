# Author - Michael Delasi  Saneke (Everstalk)

from random import randint

def word_guess(num_of_guesses):
    if num_of_guesses == 6:
        print("""
            _________
            |      |
            |      O
            |
            |
            |
            |
            |
        ---------
        Don't Worry keep guessing
        """)

    elif num_of_guesses == 5:
        print("""
            _________
            |      |
            |      O
            |     |||
            |
            |
            |
            |
        ---------
        Are you even trying?
        """)

    elif num_of_guesses == 4:
        print("""
            _________
            |      |
            |      O
            |     /|\
            |      |
            |
            |
            |
        ---------
        Seriously can you even spell?
        """)

    elif num_of_guesses == 3:
        print("""
            _________
            |      |
            |      O
            |    //|\\
            |      |
            |
            |
            |
        ---------
        Come on already!!!!
        """)

    elif num_of_guesses == 2:
        print("""
            _________
            |      |
            |      O
            |    //|\\
            |      |
            |
            |
            |
        ---------
        
        """)

    elif num_of_guesses == 1:
        print("""
            _________
            |      |
            |      O
            |    /|||\\
            |      |
            |     /
            |
            |
        ---------
        Dont mean to push but kinda dying here
        """)

    elif num_of_guesses == 0:
        print("""
            _________
            |      |
            |      O
            |    /|||\\
            |      |
            |     / \\
            |
            |
        ---------
        You lose.
        """)

    print("You have {} guesses left.".format(num_of_guesses))

wordlist = ["acres", "adult","film","canal","breeze","calm","customs","january",
            "habit","grandmother","garage","kids","label","hunter","mission","monkey",
            "norway","poetry","pride","recall","palace","skeleton","shout","slope",
            "thumb","solar","species","silicon","valley"]


word = wordlist[randint(0,len(wordlist))]
wordlength = len(wordlist)

guesses = 7

letters = []
for letter in word:
    letters.append(letter)

print("""

Welcome to Hangman!
    _________
    |      |
    |
    |
    |
    |
    |
    |
---------
""" +
"_ " * wordlength )

while True:
    guess = input("Guess a letter or the whole word: ")

    if guess == word:
        print("Yaye, you've won and have saved my neck!")
        break
    
    else:
        for letter in letters:
            if letter in letters:
                continue
    else:
        guesses -= 1
        word_guess(guesses)

    if guesses == 0:
        break
    

   
