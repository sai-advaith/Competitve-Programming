class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.min = []

    def push(self, x):
        self.A.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)
    def pop(self):
        num =  self.A.pop()
        if num==self.min[-1]:
            self.min.pop()
    def top(self):
        return self.A[-1]

    def getMin(self):
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()