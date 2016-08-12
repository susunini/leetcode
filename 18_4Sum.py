class Solution(object):
    """
    Solution 1: Store tuples of indexes of nums instead of nums. Why? corner cases: nums = [1, 1, 1, 1, ... ] and target = 4
    """
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        d = collections.defaultdict(list)
        r_list = list()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                d[nums[i] + nums[j]].append((i, j))
        for key in d:
            offset = target - key
            if offset in d:
                for (i, j) in d[key]:
                    for (p, q) in d[offset]:
                        if j < p:
                             r_list.append((nums[i], nums[j], nums[p], nums[q]))
        return list(set(r_list))
        
class Solution(object):
    """
    Solution 1.1:
    Same as Solution 1; except iterating nums instead of iterating the dictionary
    """
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        d = collections.defaultdict(list)
        r_list = list()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                d[nums[i] + nums[j]].append((i, j))
        for i in range(n):
            for j in range(i+1, n):
                offset = target - nums[i] - nums[j]
                if offset in d:
                    for (p, q) in d[offset]:
                        if j < p:
                            r_list.append((nums[i], nums[j], nums[p], nums[q]))
        return list(set(r_list))
