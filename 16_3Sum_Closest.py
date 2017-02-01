class Solution(object):
    """ Wrong. """
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = None
        for p1, num1 in enumerate(nums):
            p2 = p1 + 1; p3 = len(nums) - 1
            while p2 < p3:
                cur_sum = num1 + nums[p2] + nums[p3]
                if cur_sum == target:
                    return cur_sum
                if res is None or abs(target-cur_sum) < abs(target-res):
                    res = cur_sum
                if cur_sum < target:
                    p2 += 1
                else:
                    p3 -= 1
        return res
        
class Solution(object):
    """ Two Pointers. 
    
    Remember to sort nums first. """
    
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = None
        nums.sort()
        for p1, num1 in enumerate(nums):
            p2 = p1 + 1; p3 = len(nums) - 1
            while p2 < p3:
                cur_sum = num1 + nums[p2] + nums[p3]
                if cur_sum == target:
                    return cur_sum
                if res is None or abs(target-cur_sum) < abs(target-res):
                    res = cur_sum
                if cur_sum < target:
                    p2 += 1
                else:
                    p3 -= 1
        return res
