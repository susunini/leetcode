class Solution(object):
    """ Bucket sort. 
    
    buckets(list) index: citation; value: freq of citation;
    size of buckets is (n+1) instead of (max_citaion+1) because 
    the answer will not be larger than n.
    """
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        buckets = [0]*(n+1) 
        for c in citations:
            if c > n:
                buckets[-1] += 1
            else:
                buckets[c] += 1
        prev = 0
        for c in range(len(buckets)-1, -1, -1):
            if buckets[c] + prev >= c:
                return c
            prev = buckets[c] + prev
        return 0
