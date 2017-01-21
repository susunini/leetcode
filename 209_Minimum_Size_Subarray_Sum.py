class Solution(object):
    """ Two Pointers. """
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = len(nums) + 1
        head = 0; cur_sum = 0
        for tail, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= s:
                min_len = min(min_len, tail - head + 1)
                cur_sum -= nums[head]
                head += 1
        return min_len if min_len != len(nums) + 1 else 0
