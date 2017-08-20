class Solution:
    def partitionArray(self, nums, k):
        """
        @param nums: The integer array you should partition
        @param k: As description
        @return: The index after partition
        """
        if not nums:
            return 0
        p1 = 0; p2 = len(nums)-1
        while p1 <= p2: # Wrong: while p1 < p2
            if nums[p1] < k:
                p1 += 1
            elif nums[p2] >= k:
                p2 -= 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1; p2 -= 1
        return p1 # return p1
