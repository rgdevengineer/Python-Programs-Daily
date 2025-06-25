
'''
Given n non-negative integers a1, a2, ..., an where each represents a point at coordinate (i, ai). 
n vertical lines are drawn. Find two lines that together with the x-axis form a container, 
such that the container contains the most water.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
'''

def max_area(height):
    
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        area = h * w
        max_water = max(max_water, area)

        # Move the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
