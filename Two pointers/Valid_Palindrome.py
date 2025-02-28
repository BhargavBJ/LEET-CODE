class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' This brute force approach that has O(N) Time and space complexity Probably the easiest solution '''
        li=[]
        for i in range(len(s)):
            if (s[i] >= 'a' and s[i]<='z') or (s[i]>='A' and s[i] <='Z') or (s[i].isnumeric()):
            # Or if s[i].isalnum():
                li.append(s[i].lower())
            else:
                continue
        return li == li[::-1]

#Link : https://leetcode.com/problems/valid-palindrome/
