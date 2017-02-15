def Collatz(number):

    if number % 2 == 0 :
        
       return print(number//2)
    elif number % 2 == 1:
        
        return print(3 * number + 1)
        
for i in range(10):
    print("Enter the number")
    try:
        Collatz(int(input()))
    except ValueError:
        print("Enter int value")
        
        
    
    
    
    
        
    
            

    
    
