#from types import List
class Solution:
    def encode(self, strs: list[str]) -> str:
        li=[]
        for i in strs:
            li.append(str(len(i)))
            li.append(i)
            li.append(str(0))
        a = ''.join((li))
        return (a)
    def decode(self, s: str) -> list[str]:
        l=[]
        i=0
        while(i< len(s)):
            if s[i].isnumeric():
                a=(int)(s[i])
                li=[]
                for j in range(0,a):
                    if s[i+j]==0:
                        break
                    li.append(s[1+i+j])
                a=''.join(li) if li else None
                l.append(a)
            i+=1
        for i in l:
            if i==None:  
                l.remove(i)
        return l
        
#Link if you do not have premium access in leetcode: https://neetcode.io/problems/string-encode-and-decode
#Official leetcode Link:https://leetcode.com/problems/encode-and-decode-strings/description/


