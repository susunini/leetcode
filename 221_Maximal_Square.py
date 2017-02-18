class Solution(object):
    """ Wrong. """
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*(m+1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if matrix[i-1][j-1] != 0:
                    dp[i][j] = min([dp[i-1][j-1], dp[i-1][j], dp[i][j-1]])
                    res = max(res, dp[i][j])
        return res * res

       

class Solution(object):
    """ Dynamic Programming.
    
    dp[i][j]: maximum size length of any square having matrix[i][j] as its right-bottom corner.
    dp[i][j] = 0 if matrix[i][j] == 0
             = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    => dp[i][j] = 0 if matrix[i-1][j-1] == 0
                = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
       dp[i][0] = 0 for i from 0 to n
       dp[0][j] = 0 for j from 0 to m
    return maximum element of dp  
    
    TODO: Space O(n^2) => O(n)
    """
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*(m+1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if matrix[i-1][j-1] != '0':
                    dp[i][j] = min([dp[i-1][j-1], dp[i-1][j], dp[i][j-1]]) + 1
                    res = max(res, dp[i][j])
        return res * res
