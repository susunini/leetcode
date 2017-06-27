class Solution(object):
    """ Heap. """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
        h = [[-val, key] for key, val in dic.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]
        
class Solution(object):
    """ Heap. """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
        h = [[val, key] for key, val in dic.items()]
        return [key for val, key in heapq.nlargest(k, h)]
