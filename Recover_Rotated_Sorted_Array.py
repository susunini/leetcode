class Solution:
    """ Wrong for test case: [1,2,3,4,5] """
    def reverseArray(self, nums, start, end):
        p1 = start; p2 = end
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1; p2 -= 1
            
    def recoverRotatedSortedArray(self, nums):
        n = len(nums)
        self.reverseArray(nums, 0, n-1)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                self.reveseArray(nums, 0, i-1)
                self.reverseArray(nums, i, n-1)
                
class Solution:
    def reverseArray(self, nums, start, end): # Wrong: def reverseArray(self, nums) Python:  slicing a list will create a new list
        p1 = start; p2 = end
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1; p2 -= 1
            
    def recoverRotatedSortedArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                self.reverseArray(nums, 0, i-1)
                self.reverseArray(nums, i, len(nums)-1)
                self.reverseArray(nums, 0, len(nums)-1)
                return # Miss
                
