from heapq import heappush, heappop

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        
    def balance(self):
        max_heap = self.max_heap
        min_heap = self.min_heap
        if abs(len(max_heap) - len(min_heap)) <= 1:
               return 
        elif len(min_heap) > len(max_heap):
               heappush(max_heap, -heappop(min_heap))
        else:
               heappush(min_heap, -heappop(max_heap))
               
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        max_heap = self.max_heap
        min_heap = self.min_heap
        if max_heap and num <= -max_heap[0]:
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)
        self.balance()

    def findMedian(self):
        """
        :rtype: float
        """
        max_heap = self.max_heap
        min_heap = self.min_heap
        if len(min_heap) == len(max_heap):
            return (-max_heap[0]+ min_heap[0])/float(2)
        if len(min_heap) > len(max_heap):
            return min_heap[0]
        else:
            return -max_heap[0]
