class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][1] = 0
        dp[n][0] = -float('inf')
        
        for index in range(n - 1, -1, -1):
            for isEven in range(2):
                performOperation = dp[index + 1][isEven ^ 1] + (nums[index] ^ k)
                dontPerformOperation = dp[index + 1][isEven] + nums[index]
                dp[index][isEven] = max(performOperation, dontPerformOperation)
        
        return dp[0][1]

  # Link : https://leetcode.com/problems/find-the-maximum-sum-of-node-values/?envType=daily-question&envId=2025-05-23
