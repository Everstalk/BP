
def fibo():
    N = int(input("Enter a number to compute terms for fibonacci sequence: "))
    f1 = 0
    f2 = 1
    
    fiboSum = 0
    
    for i in range(1,N+1):
        f1 = f2
        f2 = fiboSum
        fiboSum = f1 + f2
    
    print(fiboSum)

fibo()
