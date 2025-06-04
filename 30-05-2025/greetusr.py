# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:30:52 2025

@author: ritwi
"""

# write a function that greets a user. If no name is provided, it should greet with a default name

def greet(name="User"):
    return "Hello " + name + "!"

print(greet(name="Python"))

print(greet())
