# Author - Michael Delasi Saneke (Everstalk)

from random import randint

randnum = randint(1,100)
guess = 0
def game():
    
    numguess = int(input("Guess the hidden the number between 1 and 100: \n"))

    if numguess == randnum:
        print ("Congrats! you've guessed correctly")
        global guess
        guess += 1
        print ("You took ",guess," guesses to get it right")
        again()
    elif numguess > randnum:
        print ("Your guess is too high, keep trying")
        global guess
        guess += 1
        game()
    elif numguess < randnum:
        print ("Your guess is too low, keep trying")
        global guess
        guess += 1
        game()
    else:
        print ("Oops,please choose a number between 1 and 100 trying ")
        game()
def again():
    ans = str(input("Would you like to play again? (y/n)\n").lower())
    if ans == 'y':
        game()
    elif ans == 'n':
        print ("Goodbye, have a nice day!")
    else:
        print ("I'm sorry, didn't catch that")
        again()

print ("Welcome to Higher Lower Guessing Game ")
game()
