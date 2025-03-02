from typing import List

from matplotlib.cbook import index_of
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0,len(numbers)-1
        while l<r:
            s = numbers[l]+numbers[r]
            if s>target:
                r-=1
            elif s<target:
                l+=1
            elif s == target:
                a = numbers.index(numbers[l])
                b = numbers.index(numbers[r])
                return [a+1,b+1]
        return []
    
