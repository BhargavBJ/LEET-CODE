from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        for i in matrix:
            for j in i:
                if j==target:
                    return True
        return False'''
        for i in matrix:
            if target in i:
                return True
        return False

#Link : https://leetcode.com/problems/search-a-2d-matrix/
