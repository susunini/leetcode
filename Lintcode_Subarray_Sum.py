class Solution:
    """Array. Prefix Sum. 
    sum[i,j] = sum[0,j] - sum[0,i].
    """
    def subarraySum(self, nums):
        """
        @param nums: A list of integers
        @return: A list of integers includes the index of the first number 
        and the index of the last number
        """
        sum_to_index = {0: -1}
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            if sum in sum_to_index:
                return [sum_to_index[sum]+1, i]
            sum_to_index[sum] = i
