class Solution(object):
    """ Backtracing. """
    def helper(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(permutation[:])
            return
        for i, num in enumerate(nums):
            if visited[i]:
                continue
            visited[i] = True
            self.helper(nums, visited, permutation+[num], permutations)
            visited[i] = False
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        visited = [False]*n
        permutations = []
        self.helper(nums, visited, [], permutations)
        return permutations
       
class Solution(object):
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
# one-liner
# https://discuss.leetcode.com/topic/17277/one-liners-in-python
