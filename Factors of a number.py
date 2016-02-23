#Author - Everstalk

num = int(input("Enter a number to generate its factors: "))
ls = []
def factor(num):
    for i in range(1,num):
        if num % i == 0:
            ls.append(i)
    if len(ls) == 1:
        print(num," is a prime number")
    ls.append(num)
    print(ls)

factor(num)
        
    
