class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0 
        for i in arr:
            if i%2 != 0:
                count+=1
                if count == 3:
                    return True
            else:
                count =0
        if count == 3:
            return True
        return False

  # Link : https://leetcode.com/problems/three-consecutive-odds/?envType=daily-question&envId=2025-05-11
