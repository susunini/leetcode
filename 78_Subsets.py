class Solution:
    """ 4%. """
    def subsets(self, nums):
        nums.sort()
        r_subsets = list()
        for i in range(1 << len(nums)):
            j = i; k = 0
            cur_subset = list()
            while j:
                if j & 1:
                    cur_subset.append(nums[k])
                j = j >> 1; k += 1
            r_subsets.append(cur_subset)
        return r_subsets
