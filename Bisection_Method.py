#Implementation of Bisection method
#Caleb Bessit
#12 March 2023

import math

#Setting global variables
tol = 0
a   = 0
b   = 0
f_x = ""

#Evaluates function
def func(x):
    return eval(f_x)

#Checking if root
def is_root(x):
    if abs(func(x))<tol:
        return True
    else: return False
    
    
def main():
    global tol
    global a
    global b
    global f_x
    
    #Get function and initial range
    f_x = input("Enter the function, f(x): ")
    a   = eval(input("Enter the lower bound of the closed interval: "))
    b   = eval(input("Enter the upper bound of the closed interval: "))
    
    #Determine whether iteration will be based on tolerance or steps
    
    if input("Iterate to a set tolerance or steps? <T/S> ")=="T":
        tol =eval(input("Enter the tolerance: "))
        i=0
        
        print("x0" + "\t: " + str(a))
        print("x1" + "\t: " + str(b))
        c = a + (b-a)/2
        while not(is_root(c)):
            i+=1
            if func(a)*func(b)>0:
                print("Interval no longer contains root.")
                break
            c = a + (b-a)/2
            
            if is_root(c):
                print("Root found! x{:d}= {:.5f}".format(i, c) )
                break
            
            print("x"+str(i) + "\t: " + str(c)) 
            
            if func(a)*func(c)<0:
                b=c
            else:
                a=c            
    
    else: 
        i=1
        steps = int(input("Enter the number of steps: "))
        
        print("x0" + "\t: " + str(a))
        print("x1" + "\t: " + str(b))
        while i<steps:
            i+=1
            if func(a)*func(b)>0:
                print("Interval no longer contains root.")
                break
            c = a + (b-a)/2
            
            if is_root(c):
                print("Root found! x{:d}= {:.5f}".format(i, c) )
                break
            
            print("x"+str(i) + "\t: " + str(c)) 
            
            if func(a)*func(c)<0:
                b=c
            else:
                a=c
            
    

if __name__=="__main__":
    main()