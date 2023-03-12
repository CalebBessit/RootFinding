#Implementation of Secant Method
#Caleb Bessit
#01 March 2023

import math

#Setting global parameters

f_x = ""
xn_0  = 0
xn_1  = 0
tol = 10e-10

def func(x):
    return eval(f_x)

def secondTerm():
    if abs( func(xn_1) -  func(xn_0) )<tol:
        return -1
    else:
        return func(xn_1) * (  (xn_1-xn_0)/  ( func(xn_1) -  func(xn_0)  ) )
    

def main():
    global f_x
    global xn_0
    global xn_1
    global tol
    
    #Obtain function and starting values from user
    f_x  = input("Enter the function, f(x): ") #Not secure, but assume user does not abuse
    
    xn_0 = eval(input("Enter the value of the first starting point: "))
    xn_1 = eval(input("Enter the value of the second starting point: "))
    
    #Determine preferred iteration conditions
    if input("Iterate to set tolerance or steps? <T/S> ")=="T":
        tol = eval(input("Enter the tolerance: "))
        i = 1
        
        print("x0\t: "+ str(xn_0))
        print("x1\t: "+ str(xn_1))
    
        while abs( xn_1-secondTerm() )>tol:
            #Update
            second = secondTerm()
            xn_0 = xn_1
            xn_1 = xn_1-second
            
            #Display
            i+=1
            print("x"+str(i) + "\t: " + str(xn_1) )
    else:
        steps = int(input("Enter the number of steps: "))
        i=1
        print("x0\t: "+ str(xn_0))
        print("x1\t: "+ str(xn_1))        
        
        while i<steps:
            #Update
            second = secondTerm()
            if second==-1:
                print("Tolerance exceeded.")
                break
            else:
                xn_0 = xn_1
                xn_1 = xn_1-second          
                
                #Display
                i+=1
                print("x"+str(i) + "\t: " + str(xn_1))      
            

if __name__ == "__main__":
    main()
        
    
    
    
    