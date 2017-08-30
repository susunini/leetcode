class Solution(object):
    """ Greedy. """
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_reach = 0; jump = 0
        i = 0
        while i < len(nums):
            if max_reach >= (len(nums)-1):
                return jump
            max_index = max_reach
            for j in range(i, max_index+1):
                max_reach = max(max_reach, j+nums[j])
            i = max_index+1
            jump += 1
            
