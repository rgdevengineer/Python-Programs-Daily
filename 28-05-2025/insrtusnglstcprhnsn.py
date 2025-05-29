# -*- coding: utf-8 -*-
"""
Created on Wed May 28 21:48:53 2025

@author: ritwi
"""

#  Insert Using List Comprehension

lst = [10,20,32,43]

new_lst = [x if x!= 32 else [2.5,x] for x in lst]

print(new_lst)

# flat = [item for sublist in new_lst for item in (sublist if isinstance(sublist, list) else [sublist])]
# flat = [10, 20, 2.5, 32, 43]
