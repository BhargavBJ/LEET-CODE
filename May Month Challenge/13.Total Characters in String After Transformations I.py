class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for _ in range(t):
            z_count = freq[25]
            for i in range(25, 0, -1):
                freq[i] = freq[i - 1]
            freq[0] = z_count % MOD
            freq[1] = (freq[1] + z_count) % MOD
        return sum(freq) % MOD

  # Link : https://leetcode.com/problems/total-characters-in-string-after-transformations-i/?envType=daily-question&envId=2025-05-13
