# Author - Michael Delasi Saneke (Everstalk)

def playloop():
    again = input("will you play again? (y/n)\n").lower()
    if again == 'y':
        triples()
    elif again == 'n':
        print ("Bye then!")
    else:
        print ("Sorry i don't get you, try again.")
        playloop()


def triples():
    while True:
        try:
            side1 = int(input("Enter first side: ")) ** 2
            side2 = int(input("Enter second side: ")) ** 2
            side3 = int(input("Enter third side: ")) ** 2
        except ValueError:
             print ("\nSorry that is not a number. \n")
        else :
             break
    
    triangle = [side1,side2,side3]
    hyp = max(triangle)
    triangle.remove(hyp)

    if sum(triangle) == hyp:
        print("You have a pythagorean triple.")
    else:
        print("You dont have a pythagorean triple.")

    playloop()

triples()    
        
