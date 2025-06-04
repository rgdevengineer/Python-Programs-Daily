# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 11:25:16 2025

@author: ritwi
"""

# Variable length non-keywords argument

def argfun(*argv):
    for arg in argv:
        print(arg)
        
argfun('Hello','Welcome','to','Python')