
'''
Challenge 2: Calculate Sine, Cosine, and Tangent of User Input
In this challenge, you are required to calculate the sine, cosine, and tangent of variable x.

Problem Statement
Use the calculateSinCosTan() function; it takes a number x as a parameter and shows the result of the sine, cosine, and tangent of the number.

Input
A number

Output
Calculate the sine, cosine, and tangent of that number

Sample Input
0

Sample Output
[0, 1, 0]
'''

import math
def calculateSinCosTan(x):
  sine = math.sin(x) #calculate sine
  cos = math.cos(x) #calculate cosine
  tan = math.tan(x) #calculate tangent 
  return [sine, cos, tan]
  