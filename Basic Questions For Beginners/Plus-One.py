class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        li =[]
        n = len(digits)
        s = 0
        for d in digits:
            s = s *10 +d
        print(s)
        s += 1
        while s>0:
            li.append(s%10)
            s//=10
        return li[::-1]