# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""
# average of a list

def average(nums):
    return sum(nums) / len(nums) if nums else 0

print(average([10, 20, 30]))  # 20.0
