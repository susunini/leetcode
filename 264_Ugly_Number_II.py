from heapq import heappop, heappush

class Solution(object):
    """ Heap. TODO: DP. """
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        visited = {1: True}
        while 1:
            min_num = heappop(heap)
            n -= 1
            if n == 0:
                return min_num
            for num in [min_num*2, min_num*3, min_num*5]:
                if num in visited:
                    continue
                visited[num] = True
                heappush(heap, num)
