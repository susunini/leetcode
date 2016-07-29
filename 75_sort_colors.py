# Note:
# At any time, A[0:i] all 0, A[i:j] all 1, A[k+1:] all 2

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0; k = len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1; j += 1
            elif nums[j] == 1:
                j += 1
            else: # nums[j] == 2
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
