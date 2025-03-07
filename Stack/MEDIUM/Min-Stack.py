class MinStack:

    def __init__(self):
        self.stack =[]
        self.mins =[]

    def push(self, val: int) -> None:
        self.stack.append(val)        
        val = min(val,self.mins[-1] if self.mins else val)
        self.mins.append(val)

    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#Link : https://leetcode.com/problems/min-stack/submissions/1565903223/
