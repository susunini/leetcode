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
    
class Solution(object):
    """ Bucket Sort. """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
        
        max_freq = max([value for _, value in dic.items()])   
        buckets = [[] for i in range(max_freq + 1)]
        for num, cnt in dic.items():
            buckets[cnt].append(num)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(res) == k:
                return res
            if buckets[i]:
                res.extend(buckets[i])
