class MinStack(object):
    """ Two Stacks. """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.min_stack.append(x if not self.min_stack else min(x, self.min_stack[-1]))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
