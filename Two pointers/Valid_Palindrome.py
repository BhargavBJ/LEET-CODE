class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' This brute force approach that has O(N) Time and space complexity Probably the easiest solution '''
        '''
        li=[]
        for i in range(len(s)):
            if (s[i] >= 'a' and s[i]<='z') or (s[i]>='A' and s[i] <='Z') or (s[i].isnumeric()):
            # Or if s[i].isalnum():
                li.append(s[i].lower())
            else:
                continue
        return li == li[::-1] '''
        
         '''This is the 2-pointer approach which has the same time complexity but has less space complexity[O(1)]'''
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

#Link : https://leetcode.com/problems/valid-palindrome/
