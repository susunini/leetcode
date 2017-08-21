class Solution:
    def findFirstEqualorLarger(self, nums, target):
        """
        @param: A: An integer array
        @param: queries: The query list
        @return: The number of element in the array that are smaller that the given integer
        """
        if not nums:
            return 0
        start = 0; end = len(nums)-1
        while start+1 < end:
            mid = start+(end-start)/2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return end+1
                
    def countOfSmallerNumber(self, A, queries):
        result = []
        A.sort()
        for num in queries:
            result.append(self.findFirstEqualorLarger(A, num))
        return result
