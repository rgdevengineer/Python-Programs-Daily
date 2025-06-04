# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 20:44:00 2025

@author: ritwi
"""
# Convert a Sentence to Title Case
def to_title_case(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

print(to_title_case("this is a test"))  
