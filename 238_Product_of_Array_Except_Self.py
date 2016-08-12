""" Easy DP problem """

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        r_nums = [1] * n
        # from left to right
        for i in range(1, n):
            r_nums[i] = r_nums[i-1] * nums[i-1]
        # from right to left
        product_right = 1
        for i in range(n-1, -1, -1):
            r_nums[i] *= product_right
            product_right *= nums[i]
        return r_nums
