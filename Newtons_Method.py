#Newton's method implementation
#Caleb Bessit
#01 March 2023
import math

#Setting global function and derivative strings
f_x     = ""
f_prime = ""
tol     = 0

#Function
def func(x):
    return eval(f_x)

#Derivative    
def deriv(x):
    return eval(f_prime)

#Checking if root
def is_root(x):
    if abs(func(x))<tol:
        return True
    else: return False

def main():
    #Getting function
    global f_x
    global f_prime
    global tol
    f_x = input("Enter the function, f(x): ")
    
    #Getting derivative
    f_prime = input("Enter the derivative, f'(x): ")
    
    #Getting guess
    x_n1 = eval(input("Enter the initial guess, x0: "))
    
    
    
    
    #Determine whether iteration will be based on tolerance or steps
    
    if input("Iterate to a set tolerance or steps? <T/S> ")=="T":
        tolerance =eval(input("Enter the tolerance: "))
        i=0
        
        print("x"+str(i) + "\t: " + str(x_n1))
        while not(is_root(x_n1, tolerance)):
            #Update
            x_n1 = x_n1 - ( func(x_n1) )/( deriv(x_n1) )
            
            #Print
            i+=1
            print("x"+str(i) + "\t: " + str(x_n1))        
    
    else: 
        i=0
        steps = int(input("Enter the number of steps: "))
        
        print("x"+str(i) + "\t: " + str(x_n1))
        while i<steps:
            x_n1 = x_n1 - ( func(x_n1) )/( deriv(x_n1) )
            i+=1
            print("x"+str(i) + "\t: " + str(x_n1))          
    
        
           
        
        
        
if __name__=="__main__":
    main()
        
        
        
        
    
    



