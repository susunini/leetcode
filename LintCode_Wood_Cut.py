class Solution:
    """ Binary Search. """
    def getCount(self, L, length):
        result = 0
        for wood_length in L:
            result += wood_length/length
        return result
            
    def woodCut(self, L, k):
        """
        @param: L: Given n pieces of wood with length L[i]
        @param: k: An integer
        @return: The maximum length of the small pieces
        """
        if not L:
            return 0
        start = 1; end = max(L)
        while start+1 < end:
            mid = start+(end-start)/2
            count = self.getCount(L, mid)
            if count >= k:
                start = mid
            else:
                end = mid
        if self.getCount(L, end) >= k:
            return end
        if self.getCount(L, start) >= k:
            return start
        return 0
