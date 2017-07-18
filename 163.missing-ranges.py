#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges
#
# Medium (24.79%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
#
# Given a sorted integer array where the range of elements are in the inclusive
# range [lower, upper], return its missing ranges.
#
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2",
# "4->49", "51->74", "76->99"].
#
#
class Solution(object):
    """ Google. """
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            return [self.helper(lower, upper)]
        res = []
        if nums[0] > lower:
            res.append(self.helper(lower, nums[0]-1))
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] > 1:
                res.append(self.helper(nums[i-1]+1, nums[i]-1))
        if nums[-1] < upper:
            res.append(self.helper(nums[-1]+1, upper))
        return res

    def helper(self, low, up):
        if low == up:
            return str(low)
        return str(low) + '->' + str(up)
