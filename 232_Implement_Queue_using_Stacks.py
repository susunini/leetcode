class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = list()
        self.stack2 = list()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        
    def pour(self, stack1, stack2):
        """ Pull from stack1 to stack2 """
        while stack1:
            stack2.append(stack1.pop())
            
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.pour(self.stack1, self.stack2)
        result = self.stack2.pop()
        self.pour(self.stack2, self.stack1)
        return result
        
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.pour(self.stack1, self.stack2)
        result = self.stack2[-1]
        self.pour(self.stack2, self.stack1)
        return result
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
