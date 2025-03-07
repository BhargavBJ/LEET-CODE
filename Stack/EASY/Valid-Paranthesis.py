class Solution:
    def isValid(self, s: str) -> bool:
        ch = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in ch:
                if stack and stack[-1] == ch[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack #Returns True only when all the elemets in the stack is popped, i.e, The stack is empty

#Link: https://leetcode.com/problems/valid-parentheses/description/
