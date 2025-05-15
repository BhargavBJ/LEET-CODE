class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s=sorted(s)
            t=sorted(t)
            if s==t:
                return True
        return False

#Link : https://leetcode.com/problems/valid-anagram/
