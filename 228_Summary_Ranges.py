class Solution(object):
    """ Array. 56%. Shorter?
    Test Cases: 1. [] 2. [1] 3. [0,1,2,4,5,7] """
    def generateRange(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        return str(nums[0]) + '->' + str(nums[-1])
    
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        p1 = 0; p2 = 0
        res = []
        while p2 < n:
            while p2 < n-1 and nums[p2+1]-nums[p2] == 1:
                p2 += 1
            res.append(self.generateRange(nums[p1:p2+1]))
            p2 += 1; 
