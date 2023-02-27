#Newton's method implementation
import math

#Function
def func(x):
    return (1-x)/(1+x)

#Derivative    
def deriv(x):
    return -2/( (1+x)**2 )

#Checking if root
def is_root(x, tol):
    if abs(func(x))<tol:
        return True
    else: return False

def main():
    #Getting guess
    x_n1 = eval(input("Enter the initial guess, x0: \n"))
    
    #Set tolerance
    tolerance =eval(input("Enter the tolerance: \n"))
    
    #Iteration counter
    i = 0
    
    print("x"+str(i) + "\t: " + str(x_n1))
    
    #while not(is_root(x_n1, tolerance)):
        #x_n1 = x_n1 - ( func(x_n1) )/( deriv(x_n1) )
        #i+=1
        #print("x"+str(i) + "\t: " + str(x_n1))
        
    while i<10:
        x_n1 = x_n1 - ( func(x_n1) )/( deriv(x_n1) )
        i+=1
        print("x"+str(i) + "\t: " + str(x_n1))        
        
        
        
main()
        
        
        
        
    
    



