# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def my_func(x1, x2, x3): 
    if x1+x2+x3 == 0:
        print("Not a number – denominator equals zero")
    elif not isinstance(x1, float) or not isinstance(x2, float) or not isinstance(x3, float):
        print ("Error: parameters should be float") 
    else:
        return ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
print(my_func(0, 0, 0))


#B
def convert(hours, minutes):
    if hours < 0 or minutes < 0:
        print("Input error!")
    else:
        
        return (hours*60 + minutes)*60
print(convert(0,1))
   
    
   
