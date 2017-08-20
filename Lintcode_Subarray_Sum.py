class Solution:
    """Array. Prefix Sum. 
    Prefix Sum. sum[i,j] = sum[0,j] - sum[0,i].
    The problem only expect one result.
    The problem assumes that there is always an answer.
    """
    def subarraySum(self, nums):
        """
        @param nums: A list of integers
        @return: A list of integers includes the index of the first number 
        and the index of the last number
        """
        sum_to_index = {0: -1} # Wrong for test case [-1,1], [0, ...] : sum_to_index = {}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum in sum_to_index:
                return [sum_to_index[cur_sum]+1, i] # Wrong: return [sum_to_index[cur_sum], i]
            sum_to_index[cur_sum] = i
