class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        # Build transition matrix T
        T = [[0] * 26 for _ in range(26)]
        
        for k in range(26):
            L = nums[k]
            for x in range(26):
                d = (x - k) % 26
                if d == 0:
                    d = 26
                if d > L:
                    cnt = 0
                else:
                    cnt = (L - d) // 26 + 1
                T[x][k] = cnt % MOD
        
        # Matrix exponentiation helper functions
        def multiply(A, B):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if not A[i][k]:
                        continue
                    for j in range(26):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res
        
        def matrix_power(mat, power):
            result = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            while power > 0:
                if power % 2 == 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                power //= 2
            return result
        T_power = matrix_power(T, t)
        
        # Multiply T_power with counts vector
        final = [0] * 26
        for i in range(26):
            for j in range(26):
                final[i] = (final[i] + T_power[i][j] * counts[j]) % MOD
        
        return sum(final) % MOD


#Link : https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/?envType=daily-question&envId=2025-05-14
