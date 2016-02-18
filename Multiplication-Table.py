# Author - Michael D. Saneke (Everstalk)

def table():
    for i in range(1,10):
        for j in range(1,10):
            print (str(j * i).rjust(5),end = '')
        print()

table()
        
