class MovingAverage(object):
    """ Google. 56%. """
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = []
        self.cap = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        if len(self.queue) > self.cap:
            self.queue.pop(0)
        return sum(self.queue)/float(len(self.queue))
        
class MovingAverage(object):
    """ 95%. """
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = []
        self.cap = size
        self.avg = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        if len(self.queue) > self.cap:
            self.avg = self.avg+(val-self.queue.pop(0))/float(self.cap)
        else:
            n = len(self.queue)
            self.avg = (self.avg*(n-1)+val)/float(n)
        return self.avg
