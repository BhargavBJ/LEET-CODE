#This ia also evaluation of postfix expression

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for c in tokens:
            if c == '+':
                stack.append(stack.pop()+stack.pop())
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            elif c == '-':
                stack.append(-1*(stack.pop()-stack.pop()))
                ''' OR
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)'''
            elif c == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]

# Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
