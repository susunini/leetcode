class Solution(object):
    """ O(m+n) """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n < 1:
            return False
        m = len(matrix[0])
        if m < 1:
            return False
        i = 0; j = m - 1
        while i < n and j >= 0:
            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False
