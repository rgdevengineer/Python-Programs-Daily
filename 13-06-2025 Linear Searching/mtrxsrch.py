
'''
Count negative numbers in a sorted matrix

Description:
You are given an m x n matrix grid where each row and column is sorted in non-increasing order. Your task is to return the number of negative numbers present in the matrix.
Parameters:
grid (List[List[int]]): A 2D matrix with dimensions m x n, where each row and each column is sorted in non-increasing order.
Return Values:
Integer: The count of negative numbers in the matrix.
Example:

Input: grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
Output: 7 
Explanation: There are 7 negative numbers in the matrix.
 
Input: grid = [[3, 2], [1, 0]] 
Output: 0 
Explanation: There are no negative numbers in the matrix.
'''

def countNegatives(grid):
    """
    Count the number of negative numbers in a matrix sorted in non-increasing order
    both row-wise and column-wise using binary search.

    Parameters:
    grid (List[List[int]]): 2D matrix with rows and columns sorted in non-increasing order.

    Returns:
    int: Total count of negative numbers in the matrix.
    """

    def count_negatives_in_row(row):
        """
        Use binary search to count the number of negative numbers in a row.
        The row is sorted in decreasing order.

        Returns:
        int: Count of negative numbers in the row.
        """
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] < 0:
                right = mid  
            else:
                left = mid + 1  
        
        return len(row) - left

    total_negatives = 0
    for row in grid:
        total_negatives += count_negatives_in_row(row)

    return total_negatives


if __name__ == "__main__":
    grid1 = [
        [4, 3, 2, 1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]
    ]
    print("Output:", countNegatives(grid1)) 

    grid2 = [
        [3, 2],
        [1, 0]
    ]
    print("Output:", countNegatives(grid2))  
