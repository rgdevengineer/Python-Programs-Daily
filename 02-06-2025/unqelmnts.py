# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""
# find unique elements in a list

def unique_elements(list1, list2):
    return list(set(list1) ^ set(list2))  

print(unique_elements([1,2,3], [2,3,4]))  
