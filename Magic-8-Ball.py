#Author - Michael Delasi Saneke (Everstalk) 

from time import sleep
from random import randint

response = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Quite possibly so",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"]

def game():
    ques = str(input("What is your question? \n").lower())
    print ("thinking...")
    sleep(1)
    print (response[randint(0,20)])
    playloop()





def playloop():
    ques_again = str(input("Would you like to ask another question? (y/n)\n").lower())
    if ques_again == 'y':
        game()

    elif ques_again == 'n':
        print("Goodbye!, come back soon")

    else: 
        print ("What was that?/n")
        loop()


game()        
