class Solution(object):
    """ Bit Manipulation. 278 secs """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            i = i | (1 << num)
        res = 0
        while 1:
            if i & 1 == 0:
                return res
            i >>= 1
            res += 1
            
class Solution(object):
    """ Bit Manipulation. Faster. """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for integer in range(len(nums)):
            res ^= integer
        for num in nums:
            res ^= num
        return res
            
 class Solution(object):
    """ Math. """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1: 
            return 0
        min_num = min(nums)
        if min_num > 0:
            return 0
            
        sum_of_nums = sum(nums)
        max_num = max(nums)
        if max_num / 2 == 0:
            sum_complete = (1 + max_num) * max_num / 2 
        else:
            sum_complete = (1 + max_num + 1) * (max_num + 1) / 2 - (max_num + 1)
        diff = sum_complete - sum_of_nums
        if diff != 0:
            return diff
        else:
            return max_num + 1
