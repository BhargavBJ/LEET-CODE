class Solution:
    def isPalindrome(self, s: str) -> bool:
        li=[]
        for i in range(len(s)):
            if (s[i] >= 'a' and s[i]<='z') or (s[i]>='A' and s[i] <='Z') or (s[i].isnumeric()):
                li.append(s[i].lower())
            else:
                continue
        return li == li[::-1]