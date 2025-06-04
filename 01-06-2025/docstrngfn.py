# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 18:12:30 2025

@author: ritwi
"""

# Adding Docstring to the function

def evenOdd(x):
    """This function will check whether the function is even or odd"""
    
    if(x % 2) == 0:
        print("Even")
    else:
        print("Odd")
        
print(evenOdd.__doc__)