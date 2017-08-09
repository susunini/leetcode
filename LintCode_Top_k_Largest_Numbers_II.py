from heapq import heappush, heappop

class Solution:
    """ Heap. """
    def __init__(self, k):
        self.k = k
        self.heap = []
 
    def add(self, num):
        heappush(self.heap, num)
        if len(self.heap) > self.k:
            heappop(self.heap)
       
    def topk(self):
        return self.heap
