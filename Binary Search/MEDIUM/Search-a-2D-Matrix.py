from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      #Brute Force with time complexity O(M*N) M- No. of rows, N- No. of columns & Space complexity: O(1)
      '''
        for i in matrix:
            for j in i:
                if j==target:
                    return True
        return False'''
      #Binary Search with time complexity O(log(M*N)) and Space Complexity O(1)
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False

  #Link : https://leetcode.com/problems/search-a-2d-matrix/
