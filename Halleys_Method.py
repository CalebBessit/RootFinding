#Implementation of Halley's Method
#Caleb Bessit
#12 March 2023

import math

#Global variables
f_x      = ""
f_prime  = ""
f_2prime = ""
tol      = 10e-8

#Function evaluation
def func(x):
    return eval(f_x)

#Derivative evaluation
def deriv(x):
    return eval(f_prime)

#2nd Derivative evaluation
def secDeriv(x):
    return eval(f_2prime)

#Second term of update formula
def secondTerm(x):
    if (func(x) * deriv(x))<tol or (  2* ( deriv(x) )**2  - func(x)*secDeriv(x) )<tol:
        return -1 #If contribution is miniscule or we need to avoid division by zero
    else:
        return ( 2*func(x)*deriv(x) ) / (  2* ( deriv(x) )**2  - func(x)*secDeriv(x))
    
#Checking if root
def is_root(x):
    if abs(func(x))<tol:
        return True
    else: return False
    
def main():
    global f_x
    global f_prime
    global f_2prime
    global tol
    
    #Get function, first and second derivatives; initial guess
    f_x = input("Enter the function, f(x): ")
    f_prime = input("Enter the first derivative, f'(x): ")    
    f_2prime = input("Enter the second derivative, f''(x): ") 
    
    x_n1 = eval(input("Enter the initial guess, x0: "))
    
    #Determine whether iteration will be based on tolerance or steps
    
    if input("Iterate to a set tolerance or steps? <T/S> ")=="T":
        tol = float(input("Enter the tolerance: "))
        i=0
        
        print("x"+str(i) + "\t: " + str(x_n1))
        while not(is_root(x_n1)):
            #Update
            x_n1 = x_n1 - secondTerm(x_n1)
            
            #Print
            i+=1
            print("x"+str(i) + "\t: " + str(x_n1))        
    
    else: 
        i=0
        steps = int(input("Enter the number of steps: "))
        
        print("x"+str(i) + "\t: " + str(x_n1))
        while i<steps:
            #if secondTerm(x_n1)<tol:
                #print("Tolerance exceeded.")
                #break
            x_n1 = x_n1 - secondTerm(x_n1)
            i+=1
            print("x"+str(i) + "\t: " + str(x_n1))          
    

if __name__=="__main__":
    main()
