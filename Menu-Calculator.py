# Author - Everstalk

def menu():
    print ("Here is the menu ")
    print ("-------------------------------------------")
    print ("""              1. Chicken Strips - $3.50
              2. French Fries - $2.50
              3. Hamburger - $4.00
              4. Hotdog - $3.50
              5. Large Drink - $1.75
              6. Medium Drink - $1.50
              7. Milk Shake - $2.25
              8. Salad - $3.75
              9. Small Drink - $1.25""")
 
    price = {1:3.50, 2:2.50, 3:4.00, 4:3.50, 5:1.75, 6:1.50, 7:2.25, 8:3.75, 9:1.25}
              

    order = list(map(int,input("Please make your orders, kindly space out order: \n").split()))
    
    total = 0
    for i in order:
        total += (price[i])
    print ("It costs: $",total)
    
    
def order_again():
    again = str(input("Would you like to order again? (y/n) ").lower())
    if again == 'y':
        menu()
        order_again()
    elif again == 'n':
        print ("Goodbye, please come back soon :) ")
    else:
        print ("I'm sorry i didnt quite catch that ")
        order_again()

    
    
    

 
menu()
order_again()
