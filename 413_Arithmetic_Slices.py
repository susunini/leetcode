class Solution(object):
    """ Wrong. """
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        prev_dp = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] != A[i-1] - A[i-2]:
                prev_dp = 0
            else:
                prev_dp = 2 * prev_dp if prev_dp else 1
                res += prev_dp
        return res
        
class Solution(object):
    """ Dynamic Programming. 
    for i in range(2, len(A))
    dp[i] = 0           if A[i] - A[i-1] != A[i-1] - A[i-2]
            dp[i-1] + 1 otherwise
            
    dp[0] = 0; dp[1] = 0
    """
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        prev_dp = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] != A[i-1] - A[i-2]:
                prev_dp = 0
            else:
                prev_dp += 1
                res += prev_dp
        return res
